import math

from selfdrive.controls.lib.pid import PIController
from selfdrive.controls.lib.drive_helpers import get_steer_max
from cereal import log
from common.op_params import opParams, ENABLE_LAT_PARAMS, LAT_PID_KP_BP, LAT_PID_KP_V, LAT_PID_KI_BP, LAT_PID_KI_V, LAT_PID_KF, STEER_LIMIT_TIMER

class LatControlPID():
  def __init__(self, CP, OP=None):
    if OP is None:
      OP = opParams()
    self.op_params = OP

    if CP.lateralTuning.which() == 'pid':
      k_p = (CP.lateralTuning.pid.kpBP, CP.lateralTuning.pid.kpV)
      k_i = (CP.lateralTuning.pid.kiBP, CP.lateralTuning.pid.kiV)
      k_f = CP.lateralTuning.pid.kf
    else:
      k_p = ([0], [1])
      k_i = ([0], [1])
      k_f = 1

    self.pid = PIController(k_p, k_i, k_f=k_f, pos_limit=1.0, neg_limit=-1.0,
                            sat_limit=CP.steerLimitTimer,
                            p_bp_key=LAT_PID_KP_BP, p_v_key=LAT_PID_KP_V,
                            i_bp_key=LAT_PID_KI_BP, i_v_key=LAT_PID_KI_V,
                            f_key=LAT_PID_KF, sat_key=STEER_LIMIT_TIMER,
                            OP=self.op_params, use_ops=ENABLE_LAT_PARAMS)
    self.angle_steers_des = 0.

  def reset(self):
    self.pid.reset()

  def update(self, active, CS, CP, VM, params, desired_curvature, desired_curvature_rate, lat_plan):
    pid_log = log.ControlsState.LateralPIDState.new_message()
    pid_log.steeringAngleDeg = float(CS.steeringAngleDeg)
    pid_log.steeringRateDeg = float(CS.steeringRateDeg)

    angle_steers_des_no_offset = math.degrees(VM.get_steer_from_curvature(-desired_curvature, CS.vEgo))
    angle_steers_des = angle_steers_des_no_offset + params.angleOffsetDeg

    if CS.vEgo < 0.3 or not active:
      output_steer = 0.0
      pid_log.active = False
      self.pid.reset()
    else:
      steers_max = get_steer_max(CP, CS.vEgo)
      self.pid.pos_limit = steers_max
      self.pid.neg_limit = -steers_max

      # TODO: feedforward something based on lat_plan.rateSteers
      steer_feedforward = angle_steers_des_no_offset  # offset does not contribute to resistive torque
      steer_feedforward *= CS.vEgo**2  # proportional to realigning tire momentum (~ lateral accel)

      deadzone = 0.0

      check_saturation = (CS.vEgo > 10) and not CS.steeringRateLimited and not CS.steeringPressed
      output_steer = self.pid.update(angle_steers_des, CS.steeringAngleDeg, check_saturation=check_saturation, override=CS.steeringPressed,
                                     feedforward=steer_feedforward, speed=CS.vEgo, deadzone=deadzone)
      pid_log.active = True
      pid_log.p = self.pid.p
      pid_log.i = self.pid.i
      pid_log.f = self.pid.f
      pid_log.output = output_steer
      pid_log.saturated = bool(self.pid.saturated)

    return output_steer, angle_steers_des, pid_log
