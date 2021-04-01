import math
import numpy as np

from common.realtime import DT_CTRL
from common.numpy_fast import clip, interp
from common.op_params import opParams

class INDIController():
  def __init__(self, pos_limit=None, neg_limit=None, OP=None):
    self.target_des = 0.
    self.speed = 0.

    self.pos_limit = pos_limit
    self.neg_limit = neg_limit

    A = np.array([[1.0, DT_CTRL, 0.0],
                  [0.0, 1.0, DT_CTRL],
                  [0.0, 0.0, 1.0]])
    C = np.array([[1.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0]])

    # Q = np.matrix([[1e-2, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 10.0]])
    # R = np.matrix([[1e-2, 0.0], [0.0, 1e3]])

    # (x, l, K) = control.dare(np.transpose(A), np.transpose(C), Q, R)
    # K = np.transpose(K)
    K = np.array([[7.30262179e-01, 2.07003658e-04],
                  [7.29394177e+00, 1.39159419e-02],
                  [1.71022442e+01, 3.38495381e-02]])

    self.K = K
    self.A_K = A - np.dot(K, C)
    self.x = np.array([[0.], [0.], [0.]])

    if OP is None:
      OP = opParams()
    self.op_params = OP

    self.sat_count_rate = 1.0 * DT_CTRL
    self.reset()

  def reset(self):
    self.delayed_output = 0.
    self.output = 0.
    self.sat_count = 0.0
    self.speed = 0.

  def _check_saturation(self, control, check_saturation, limit):
    saturated = abs(control) == limit

    if saturated and check_saturation:
      self.sat_count += self.sat_count_rate
    else:
      self.sat_count -= self.sat_count_rate

    self.sat_count = clip(self.sat_count, 0.0, 1.0)

    return self.sat_count > self.sat_limit

  def update(self, target, current, rate_current, rate_target, speed, check_saturation=True, active=True):
    # Update Kalman filter
    y = np.array([[current], [rate_current]])
    self.x = np.dot(self.A_K, self.x) + np.dot(self.K, y)

    if speed < 0.3 or not active:
      self.output = 0.0
      self.delayed_output = 0.0
    else:
      self.target_des = target
      self.rate_des = rate_target

      target_des = self.target_des
      rate_des = self.rate_des

      # Expected actuator value
      alpha = 1. - DT_CTRL / (self.RC + DT_CTRL)
      self.delayed_output = self.delayed_output * alpha + self.output * (1. - alpha)

      # Compute acceleration error
      rate_sp = self.outer_loop_gain * (target_des - self.x[0]) + rate_des
      accel_sp = self.inner_loop_gain * (rate_sp - self.x[1])
      accel_error = accel_sp - self.x[2]

      # Compute change in actuator
      g_inv = 1. / self.G
      delta_u = g_inv * accel_error

      self.output = clip(self.delayed_output + delta_u, self.neg_limit, self.pos_limit)

    return float(self.output)
