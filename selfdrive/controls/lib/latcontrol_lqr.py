import numpy as np
from selfdrive.controls.lib.drive_helpers import get_steer_max
from common.numpy_fast import clip
from common.realtime import DT_CTRL
from common.op_params import opParams, ENABLE_LAT_PARAMS, LQR_SCALE, LQR_KI, LQR_A, LQR_B, LQR_C, LQR_K, LQR_L, LQR_DC_GAIN, STEER_LIMIT_TIMER, WHICH_LAT_CTRL
from cereal import log


class LatControlLQR():
  def __init__(self, CP, OP=None):
    if CP.lateralTuning.which() == 'lqr':
      self.scale = CP.lateralTuning.lqr.scale
      self.ki = CP.lateralTuning.lqr.ki
      self.A = np.array(CP.lateralTuning.lqr.a).reshape((2, 2))
      self.B = np.array(CP.lateralTuning.lqr.b).reshape((2, 1))
      self.C = np.array(CP.lateralTuning.lqr.c).reshape((1, 2))
      self.K = np.array(CP.lateralTuning.lqr.k).reshape((1, 2))
      self.L = np.array(CP.lateralTuning.lqr.l).reshape((2, 1))
      self.dc_gain = CP.lateralTuning.lqr.dcGain
      self.sat_limit = CP.steerLimitTimer

    self.x_hat = np.array([[0], [0]])
    self.i_unwind_rate = 0.3 * DT_CTRL
    self.i_rate = 1.0 * DT_CTRL

    self.sat_count_rate = 1.0 * DT_CTRL

    if OP is None:
      OP = opParams()

    self.op_params = OP

    self._update_params(CP)
    self.reset()

  def reset(self):
    self.i_lqr = 0.0
    self.output_steer = 0.0
    self.sat_count = 0.0

  def _check_saturation(self, control, check_saturation, limit):
    saturated = abs(control) == limit

    if saturated and check_saturation:
      self.sat_count += self.sat_count_rate
    else:
      self.sat_count -= self.sat_count_rate

    self.sat_count = clip(self.sat_count, 0.0, 1.0)

    return self.sat_count > self.sat_limit

  def _update_params(self, CP):
    if self.op_params.get(ENABLE_LAT_PARAMS) and self.op_params.get(WHICH_LAT_CTRL) == 'lqr':
      self.scale = self.op_params.get(LQR_SCALE)
      self.ki = self.op_params.get(LQR_KI)
      self.A = np.array(self.op_params.get(LQR_A)).reshape((2, 2))
      self.B = np.array(self.op_params.get(LQR_B)).reshape((2, 1))
      self.C = np.array(self.op_params.get(LQR_C)).reshape((1, 2))
      self.K = np.array(self.op_params.get(LQR_K)).reshape((1, 2))
      self.L = np.array(self.op_params.get(LQR_L)).reshape((2, 1)) 
      self.dc_gain = self.op_params.get(LQR_DC_GAIN)
      self.sat_limit = self.op_params.get(STEER_LIMIT_TIMER)
    elif CP.lateralTuning.which() == 'lqr':
      self.scale = CP.lateralTuning.lqr.scale
      self.ki = CP.lateralTuning.lqr.ki
      self.A = np.array(CP.lateralTuning.lqr.a).reshape((2, 2))
      self.B = np.array(CP.lateralTuning.lqr.b).reshape((2, 1))
      self.C = np.array(CP.lateralTuning.lqr.c).reshape((1, 2))
      self.K = np.array(CP.lateralTuning.lqr.k).reshape((1, 2))
      self.L = np.array(CP.lateralTuning.lqr.l).reshape((2, 1))
      self.dc_gain = CP.lateralTuning.lqr.dcGain
      self.sat_limit = CP.steerLimitTimer

  def update(self, active, CS, CP, path_plan):
    self._update_params(CP)

    lqr_log = log.ControlsState.LateralLQRState.new_message()

    steers_max = get_steer_max(CP, CS.vEgo)
    torque_scale = (0.45 + CS.vEgo / 60.0)**2  # Scale actuator model with speed

    steering_angle = CS.steeringAngle

    # Subtract offset. Zero angle should correspond to zero torque
    self.angle_steers_des = path_plan.angleSteers - path_plan.angleOffset
    steering_angle -= path_plan.angleOffset

    # Update Kalman filter
    angle_steers_k = float(self.C.dot(self.x_hat))
    e = steering_angle - angle_steers_k
    self.x_hat = self.A.dot(self.x_hat) + self.B.dot(CS.steeringTorqueEps / torque_scale) + self.L.dot(e)

    if CS.vEgo < 0.3 or not active:
      lqr_log.active = False
      lqr_output = 0.
      self.reset()
    else:
      lqr_log.active = True

      # LQR
      u_lqr = float(self.angle_steers_des / self.dc_gain - self.K.dot(self.x_hat))
      lqr_output = torque_scale * u_lqr / self.scale

      # Integrator
      if CS.steeringPressed:
        self.i_lqr -= self.i_unwind_rate * float(np.sign(self.i_lqr))
      else:
        error = self.angle_steers_des - angle_steers_k
        i = self.i_lqr + self.ki * self.i_rate * error
        control = lqr_output + i

        if (error >= 0 and (control <= steers_max or i < 0.0)) or \
           (error <= 0 and (control >= -steers_max or i > 0.0)):
          self.i_lqr = i

      self.output_steer = lqr_output + self.i_lqr
      self.output_steer = clip(self.output_steer, -steers_max, steers_max)

    check_saturation = (CS.vEgo > 10) and not CS.steeringRateLimited and not CS.steeringPressed
    saturated = self._check_saturation(self.output_steer, check_saturation, steers_max)

    lqr_log.steerAngle = angle_steers_k + path_plan.angleOffset
    lqr_log.i = self.i_lqr
    lqr_log.output = self.output_steer
    lqr_log.lqrOutput = lqr_output
    lqr_log.saturated = saturated
    return self.output_steer, float(self.angle_steers_des), lqr_log
