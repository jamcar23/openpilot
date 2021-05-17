from cereal import log
from common.numpy_fast import clip, interp
from selfdrive.controls.lib.pid import PIController
from common.op_params import opParams, ENABLE_COASTING, EVAL_COAST_LONG, ENABLE_LONG_PARAMS, \
                              GAS_MAX_BP, GAS_MAX_V, ENABLE_BRAKE_PARAMS, ENABLE_GAS_PARAMS, BRAKE_MAX_BP, BRAKE_MAX_V, \
                              ENABLE_LONG_PID_PARAMS, LONG_PID_KP_BP, LONG_PID_KP_V, LONG_PID_KI_BP, LONG_PID_KI_V, \
                              ENABLE_LONG_DEADZONE_PARAMS, LONG_DEADZONE_BP, LONG_DEADZONE_V, LONG_PID_KF, LONG_PID_SAT_LIMIT, \
                              ENABLE_START_STOP_PARAMS, STOP_BRAKE_RATE_BP, STOP_BRAKE_RATE_V, START_BRAKE_RATE_BP, START_BRAKE_RATE_V

LongCtrlState = log.ControlsState.LongControlState
Source = log.LongitudinalPlan.LongitudinalPlanSource

STOPPING_EGO_SPEED = 0.5
STOPPING_TARGET_SPEED_OFFSET = 0.01
STARTING_TARGET_SPEED = 0.5
BRAKE_THRESHOLD_TO_PID = 0.2

BRAKE_STOPPING_TARGET = 0.5  # apply at least this amount of brake to maintain the vehicle stationary

RATE = 100.0

def long_control_state_trans(active, long_control_state, v_ego, v_target, v_pid,
                             output_gb, brake_pressed, cruise_standstill, min_speed_can):
  """Update longitudinal control state machine"""
  stopping_target_speed = min_speed_can + STOPPING_TARGET_SPEED_OFFSET
  stopping_condition = (v_ego < 2.0 and cruise_standstill) or \
                       (v_ego < STOPPING_EGO_SPEED and
                        ((v_pid < stopping_target_speed and v_target < stopping_target_speed) or
                         brake_pressed))

  starting_condition = v_target > STARTING_TARGET_SPEED and not cruise_standstill

  if not active:
    long_control_state = LongCtrlState.off

  else:
    if long_control_state == LongCtrlState.off:
      if active:
        long_control_state = LongCtrlState.pid

    elif long_control_state == LongCtrlState.pid:
      if stopping_condition:
        long_control_state = LongCtrlState.stopping

    elif long_control_state == LongCtrlState.stopping:
      if starting_condition:
        long_control_state = LongCtrlState.starting

    elif long_control_state == LongCtrlState.starting:
      if stopping_condition:
        long_control_state = LongCtrlState.stopping
      elif output_gb >= -BRAKE_THRESHOLD_TO_PID:
        long_control_state = LongCtrlState.pid

  return long_control_state


class LongControl():
  def __init__(self, CP, compute_gb, OP=None):
    self.long_control_state = LongCtrlState.off  # initialized to off

    if OP is None:
      OP = opParams()
    self.op_params = OP

    self.pid = PIController((CP.longitudinalTuning.kpBP, CP.longitudinalTuning.kpV),
                            (CP.longitudinalTuning.kiBP, CP.longitudinalTuning.kiV),
                            rate=RATE,
                            sat_limit=0.8,
                            convert=compute_gb,
                            p_bp_key=LONG_PID_KP_BP,
                            p_v_key=LONG_PID_KP_V,
                            i_bp_key=LONG_PID_KI_BP,
                            i_v_key=LONG_PID_KI_V,
                            f_key=LONG_PID_KF,
                            sat_key=LONG_PID_SAT_LIMIT,
                            OP=self.op_params,
                            use_ops=lambda op: op.get(ENABLE_LONG_PARAMS) and op.get(ENABLE_LONG_PID_PARAMS))
    self.v_pid = 0.0
    self.last_output_gb = 0.0

  def reset(self, v_pid):
    """Reset PID controller and change setpoint"""
    self.pid.reset()
    self.v_pid = v_pid

  def update(self, active, CS, v_target, v_target_future, a_target, CP, source):
    """Update longitudinal control. This updates the state machine and runs a PID loop"""
    # Actuation limits
    gm_bp = CP.gasMaxBP
    gm_v = CP.gasMaxV
    bm_bp = CP.brakeMaxBP
    bm_v = CP.brakeMaxV
    dz_bp = CP.longitudinalTuning.deadzoneBP
    dz_v = CP.longitudinalTuning.deadzoneV
    stop_rate = CP.stoppingBrakeRate
    start_rate = CP.startingBrakeRate

    if self.op_params.get(ENABLE_LONG_PARAMS):
      if self.op_params.get(ENABLE_GAS_PARAMS):
        gm_bp = self.op_params.get(GAS_MAX_BP)
        gm_v = self.op_params.get(GAS_MAX_V)
      if self.op_params.get(ENABLE_BRAKE_PARAMS):
        bm_bp = self.op_params.get(BRAKE_MAX_BP)
        bm_v = self.op_params.get(BRAKE_MAX_V)
      if self.op_params.get(ENABLE_LONG_DEADZONE_PARAMS):
        dz_bp = self.op_params.get(LONG_DEADZONE_BP)
        dz_v = self.op_params.get(LONG_DEADZONE_V)
      if self.op_params.get(ENABLE_START_STOP_PARAMS):
        stop_rate = interp(CS.vEgo, self.op_params.get(STOP_BRAKE_RATE_BP), self.op_params.get(STOP_BRAKE_RATE_V))
        start_rate = interp(CS.vEgo, self.op_params.get(START_BRAKE_RATE_BP), self.op_params.get(START_BRAKE_RATE_V))

    gas_max = interp(CS.vEgo, gm_bp, gm_v)
    brake_max = interp(CS.vEgo, bm_bp, bm_v)

    # Update state machine
    output_gb = self.last_output_gb
    self.long_control_state = long_control_state_trans(active, self.long_control_state, CS.vEgo,
                                                       v_target_future, self.v_pid, output_gb,
                                                       CS.brakePressed, CS.cruiseState.standstill, CP.minSpeedCan)

    v_ego_pid = max(CS.vEgo, CP.minSpeedCan)  # Without this we get jumps, CAN bus reports 0 when speed < 0.3

    if self.long_control_state == LongCtrlState.off or CS.gasPressed:
      self.reset(v_ego_pid)
      output_gb = 0.

    # tracking objects and driving
    elif self.long_control_state == LongCtrlState.pid:
      self.v_pid = v_target
      self.pid.pos_limit = gas_max
      self.pid.neg_limit = - brake_max

      if self.op_params.get(ENABLE_COASTING) and self.op_params.get(EVAL_COAST_LONG):
        no_gas = source in [Source.cruiseBrake, Source.cruiseCoast]
        no_brake = source in [Source.cruiseGas, Source.cruiseCoast]

        if no_gas:
          self.pid.pos_limit = 0.

        if no_brake:
          self.pid.neg_limit = 0.

        if no_gas and no_brake:
          self.reset(CS.vEgo)

      # Toyota starts braking more when it thinks you want to stop
      # Freeze the integrator so we don't accelerate to compensate, and don't allow positive acceleration
      prevent_overshoot = not CP.stoppingControl and CS.vEgo < 1.5 and v_target_future < 0.7
      deadzone = interp(v_ego_pid, dz_bp, dz_v)

      output_gb = self.pid.update(self.v_pid, v_ego_pid, speed=v_ego_pid, deadzone=deadzone, feedforward=a_target, freeze_integrator=prevent_overshoot)

      if prevent_overshoot:
        output_gb = min(output_gb, 0.0)

    # Intention is to stop, switch to a different brake control until we stop
    elif self.long_control_state == LongCtrlState.stopping:
      # Keep applying brakes until the car is stopped
      if not CS.standstill or output_gb > -BRAKE_STOPPING_TARGET:
        output_gb -= stop_rate / RATE
      output_gb = clip(output_gb, -brake_max, gas_max)
      self.reset(CS.vEgo)
    # Intention is to move again, release brake fast before handing control to PID
    elif self.long_control_state == LongCtrlState.starting:
      if output_gb < -0.2:
        output_gb += start_rate / RATE
      self.reset(CS.vEgo)

    self.last_output_gb = output_gb
    final_gas = clip(output_gb, 0., gas_max)
    final_brake = -clip(output_gb, -brake_max, 0.)

    return final_gas, final_brake
