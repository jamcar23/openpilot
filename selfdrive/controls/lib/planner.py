#!/usr/bin/env python3
import math
import numpy as np
from common.params import Params
from common.numpy_fast import interp, incremental_avg

import cereal.messaging as messaging
from cereal import car, log
from common.realtime import sec_since_boot
from common.op_params import opParams, ENABLE_COASTING, COAST_SPEED, DOWNHILL_INCLINE, ALWAYS_EVAL_COAST
from selfdrive.swaglog import cloudlog
from selfdrive.config import Conversions as CV
from selfdrive.controls.lib.speed_smoother import speed_smoother
from selfdrive.controls.lib.longcontrol import LongCtrlState, MIN_CAN_SPEED
from selfdrive.controls.lib.fcw import FCWChecker
from selfdrive.controls.lib.long_mpc import LongitudinalMpc
from selfdrive.controls.lib.drive_helpers import V_CRUISE_MAX

LON_MPC_STEP = 0.2  # first step is 0.2s
AWARENESS_DECEL = -0.2     # car smoothly decel at .2m/s^2 when user is distracted

# lookup tables VS speed to determine min and max accels in cruise
# make sure these accelerations are smaller than mpc limits
_A_CRUISE_MIN_V = [-1.0, -.8, -.67, -.5, -.30]
_A_CRUISE_MIN_BP = [   0., 5.,  10., 20.,  40.]

# need fast accel at very low speed for stop and go
# make sure these accelerations are smaller than mpc limits
_A_CRUISE_MAX_V = [1.2, 1.2, 0.65, .4]
_A_CRUISE_MAX_V_FOLLOWING = [1.6, 1.6, 0.65, .4]
_A_CRUISE_MAX_BP = [0.,  6.4, 22.5, 40.]

# Lookup table for turns
_A_TOTAL_MAX_V = [1.7, 3.2]
_A_TOTAL_MAX_BP = [20., 40.]

Source = log.Plan.LongitudinalPlanSource


def calc_cruise_accel_limits(v_ego, following, op_params):
  min_key = "a_cruise_min_v"
  max_key = "a_cruise_max_v"

  if following:
    min_key += "_following"
    max_key += "_following"

  a_cruise_min = interp(v_ego, op_params.get('a_cruise_min_bp'), op_params.get(min_key))
  a_cruise_max = interp(v_ego, op_params.get('a_cruise_max_bp'), op_params.get(max_key))

  return np.vstack([a_cruise_min, a_cruise_max])


def limit_accel_in_turns(v_ego, angle_steers, a_target, CP):
  """
  This function returns a limited long acceleration allowed, depending on the existing lateral acceleration
  this should avoid accelerating when losing the target in turns
  """

  a_total_max = interp(v_ego, _A_TOTAL_MAX_BP, _A_TOTAL_MAX_V)
  a_y = v_ego**2 * angle_steers * CV.DEG_TO_RAD / (CP.steerRatio * CP.wheelbase)
  a_x_allowed = math.sqrt(max(a_total_max**2 - a_y**2, 0.))

  return [a_target[0], min(a_target[1], a_x_allowed)]


class Planner():
  def __init__(self, CP, OP = None):
    self.CP = CP

    self.mpc1 = LongitudinalMpc(1)
    self.mpc2 = LongitudinalMpc(2)

    self.v_acc_start = 0.0
    self.a_acc_start = 0.0

    self.v_acc = 0.0
    self.v_acc_future = 0.0
    self.a_acc = 0.0
    self.v_cruise = 0.0
    self.a_cruise = 0.0

    self.longitudinalPlanSource = Source.cruiseGas
    self.cruise_plan = Source.cruiseGas

    self.fcw_checker = FCWChecker()
    self.path_x = np.arange(192)

    self.params = Params()
    self.first_loop = True

    if OP is None:
      OP = opParams()
      
    self.op_params = OP

    self.avg_height = 0.0 # Average distance from the camera to the ground in meters
    self.height_samples = 0
    self.last_delta_height = 0.0

    self.last_incline = 0.0 # Last incline of the road in radians
    self.was_downhill = False

  def choose_solution(self, v_cruise_setpoint, enabled):
    if enabled:
      solutions = {self.cruise_plan: self.v_cruise}
      if self.mpc1.prev_lead_status:
        solutions[Source.mpc1] = self.mpc1.v_mpc
      if self.mpc2.prev_lead_status:
        solutions[Source.mpc2] = self.mpc2.v_mpc

      slowest = min(solutions, key=solutions.get)

      self.longitudinalPlanSource = slowest
      # Choose lowest of MPC and cruise
      if slowest == Source.mpc1:
        self.v_acc = self.mpc1.v_mpc
        self.a_acc = self.mpc1.a_mpc
      elif slowest == Source.mpc2:
        self.v_acc = self.mpc2.v_mpc
        self.a_acc = self.mpc2.a_mpc
      elif slowest == self.cruise_plan:
        self.v_acc = self.v_cruise
        self.a_acc = self.a_cruise

    self.v_acc_future = min([self.mpc1.v_mpc_future, self.mpc2.v_mpc_future, v_cruise_setpoint])

  def update(self, sm, pm, CP, VM, PP):
    """Gets called when new radarState is available"""
    cur_time = sec_since_boot()
    v_ego = sm['carState'].vEgo
    a_ego = sm['carState'].aEgo

    long_control_state = sm['controlsState'].longControlState
    v_cruise_kph = sm['controlsState'].vCruise
    force_slow_decel = sm['controlsState'].forceDecel

    v_cruise_kph = min(v_cruise_kph, V_CRUISE_MAX)
    v_cruise_setpoint = v_cruise_kph * CV.KPH_TO_MS

    lead_1 = sm['radarState'].leadOne
    lead_2 = sm['radarState'].leadTwo

    enabled = (long_control_state == LongCtrlState.pid) or (long_control_state == LongCtrlState.stopping)
    following = lead_1.status and lead_1.dRel < 45.0 and lead_1.vLeadK > v_ego and lead_1.aLeadK > 0.0

    # Calculate speed for normal cruise control
    if enabled and not self.first_loop and not sm['carState'].gasPressed:
      accel_limits = [float(x) for x in calc_cruise_accel_limits(v_ego, following, self.op_params)]
      jerk_limits = [min(-0.1, accel_limits[0]), max(0.1, accel_limits[1])]  # TODO: make a separate lookup for jerk tuning
      accel_limits_turns = limit_accel_in_turns(v_ego, sm['carState'].steeringAngle, accel_limits, self.CP)

      if force_slow_decel:
        # if required so, force a smooth deceleration
        accel_limits_turns[1] = min(accel_limits_turns[1], AWARENESS_DECEL)
        accel_limits_turns[0] = min(accel_limits_turns[0], accel_limits_turns[1])

      if self.op_params.get(ENABLE_COASTING):
        self.coast_speed = self.op_params.get(COAST_SPEED) * CV.MPH_TO_MS
        self.v_cruise, self.a_cruise = self.choose_cruise(sm,
                                                          v_ego,
                                                          a_ego,
                                                          v_cruise_setpoint,
                                                          accel_limits_turns,
                                                          jerk_limits)
      else:
        self.v_cruise, self.a_cruise = speed_smoother(self.v_acc_start, self.a_acc_start,
                                                    v_cruise_setpoint,
                                                    accel_limits_turns[1], accel_limits_turns[0],
                                                    jerk_limits[1], jerk_limits[0],
                                                    LON_MPC_STEP)

      # cruise speed can't be negative even is user is distracted
      self.v_cruise = max(self.v_cruise, 0.)
    else:
      starting = long_control_state == LongCtrlState.starting
      a_ego = min(a_ego, 0.0)
      reset_speed = MIN_CAN_SPEED if starting else v_ego
      reset_accel = self.CP.startAccel if starting else a_ego
      self.v_acc = reset_speed
      self.a_acc = reset_accel
      self.v_acc_start = reset_speed
      self.a_acc_start = reset_accel
      self.v_cruise = reset_speed
      self.a_cruise = reset_accel
      self.cruise_plan = Source.cruiseGas

    self.mpc1.set_cur_state(self.v_acc_start, self.a_acc_start)
    self.mpc2.set_cur_state(self.v_acc_start, self.a_acc_start)

    self.mpc1.update(pm, sm['carState'], lead_1)
    self.mpc2.update(pm, sm['carState'], lead_2)

    self.choose_solution(v_cruise_setpoint, enabled)

    # determine fcw
    if self.mpc1.new_lead:
      self.fcw_checker.reset_lead(cur_time)

    blinkers = sm['carState'].leftBlinker or sm['carState'].rightBlinker
    fcw = self.fcw_checker.update(self.mpc1.mpc_solution, cur_time,
                                  sm['controlsState'].active,
                                  v_ego, sm['carState'].aEgo,
                                  lead_1.dRel, lead_1.vLead, lead_1.aLeadK,
                                  lead_1.yRel, lead_1.vLat,
                                  lead_1.fcw, blinkers) and not sm['carState'].brakePressed
    if fcw:
      cloudlog.info("FCW triggered %s", self.fcw_checker.counters)

    radar_dead = not sm.alive['radarState']

    radar_errors = list(sm['radarState'].radarErrors)
    radar_fault = car.RadarData.Error.fault in radar_errors
    radar_can_error = car.RadarData.Error.canError in radar_errors

    # **** send the plan ****
    plan_send = messaging.new_message('plan')

    plan_send.valid = sm.all_alive_and_valid(service_list=['carState', 'controlsState', 'radarState'])

    plan_send.plan.mdMonoTime = sm.logMonoTime['model']
    plan_send.plan.radarStateMonoTime = sm.logMonoTime['radarState']

    # longitudal plan
    plan_send.plan.vCruise = float(self.v_cruise)
    plan_send.plan.aCruise = float(self.a_cruise)
    plan_send.plan.vStart = float(self.v_acc_start)
    plan_send.plan.aStart = float(self.a_acc_start)
    plan_send.plan.vTarget = float(self.v_acc)
    plan_send.plan.aTarget = float(self.a_acc)
    plan_send.plan.vTargetFuture = float(self.v_acc_future)
    plan_send.plan.hasLead = self.mpc1.prev_lead_status
    plan_send.plan.longitudinalPlanSource = self.longitudinalPlanSource

    radar_valid = not (radar_dead or radar_fault)
    plan_send.plan.radarValid = bool(radar_valid)
    plan_send.plan.radarCanError = bool(radar_can_error)

    plan_send.plan.processingDelay = (plan_send.logMonoTime / 1e9) - sm.rcv_time['radarState']

    # Send out fcw
    plan_send.plan.fcw = fcw

    pm.send('plan', plan_send)

    # Interpolate 0.05 seconds and save as starting point for next iteration
    a_acc_sol = self.a_acc_start + (CP.radarTimeStep / LON_MPC_STEP) * (self.a_acc - self.a_acc_start)
    v_acc_sol = self.v_acc_start + CP.radarTimeStep * (a_acc_sol + self.a_acc_start) / 2.0
    self.v_acc_start = v_acc_sol
    self.a_acc_start = a_acc_sol

    self.first_loop = False

  def choose_cruise(self, sm, v_ego, a_ego, v_cruise_setpoint, accel_limits_turns, jerk_limits):
    delta_h = self.last_delta_height
    incline = self.last_incline

    # Use the new depth net to calculate the incline of the road
    if sm.updated['modelV2']:
      md = sm['modelV2']

      if len(md.laneLines):
        # Get the hights of the camera at each time step from each lane line
        heights = np.array([ll.z for ll in md.laneLines])
        # Collapse heights into a 1D array containing the average height at each time step
        # weighted by the model's confidence in its lane predicitions
        heights = np.average(heights, axis=0, weights=md.laneLineProbs)

        # x and t are always the same for all lanes so just grab the first one
        steps = md.laneLines[0].t

        # Get the average forward and heights changes
        # weighted by time since we're planning for the future
        delta_x = np.average(md.laneLines[0].x, weights=steps)
        delta_h = np.average(heights, weights=steps)

        # Get the average distance from the camera to the road throughout the drive
        self.height_samples +=1
        self.avg_height = incremental_avg(self.avg_height, heights[0], self.height_samples)

        # Get the angle, in radians, between the average and future height of the camera
        # Negate because a positive angle means we're going downhill
        incline = -math.atan2(delta_h - self.avg_height, delta_x)

    # When coasting, reset plans
    if self.longitudinalPlanSource == Source.cruiseCoast:
      self.v_acc_start = v_ego
      self.a_acc_start = a_ego

    # When following return to cruiseGas
    if self.longitudinalPlanSource in [Source.mpc1, Source.mpc2]:
      self.cruise_plan = Source.cruiseGas

    # Coast continues current state
    v_coast, a_coast = v_ego + a_ego * LON_MPC_STEP, a_ego
    cruise = {Source.cruiseCoast: (v_coast, a_coast)}

    # Gas to v_cruise_setpoint
    v_gas, a_gas = speed_smoother(self.v_acc_start, self.a_acc_start,
                                  v_cruise_setpoint,
                                  accel_limits_turns[1], accel_limits_turns[0],
                                  jerk_limits[1], jerk_limits[0],
                                  LON_MPC_STEP)

    cruise[Source.cruiseGas] = (v_gas, a_gas)

    coast_setpoint = v_cruise_setpoint + self.coast_speed
    # Brake to (v_cruise_setpoint + COAST_SPEED)
    # TODO: rethink this for toyota? v_cruise_setpoint has to be lower than
    # the car's setpoint or the car will engine brake on its own.
    # In other words the max speed (with coasting) is the car's setpoint.
    v_brake, a_brake = speed_smoother(self.v_acc_start, self.a_acc_start,
                                      coast_setpoint,
                                      accel_limits_turns[1], accel_limits_turns[0],
                                      jerk_limits[1], jerk_limits[0],
                                      LON_MPC_STEP)

    cruise[Source.cruiseBrake] = (v_brake, a_brake)

    dh_incline = math.radians(self.op_params.get(DOWNHILL_INCLINE))
    is_downhill = incline < dh_incline or v_ego > v_cruise_setpoint

    # Entry conditions
    if self.op_params.get(ALWAYS_EVAL_COAST) or is_downhill or is_downhill != self.was_downhill:
      if is_downhill:
        self.cruise_plan = Source.cruiseCoast if v_ego < coast_setpoint else Source.cruiseBrake
      else:
        self.cruise_plan = Source.cruiseGas

    cloudlog.info("Cruise Plan %s: ego(%f,%f) gas(%f,%f) coast(%f,%f) brake(%f,%f) delta_h(%f) incline(%f) is_downhill(%s) was_downhill(%s)",
                  self.cruise_plan, v_ego, a_ego, v_gas, a_gas, v_coast, a_coast,
                  v_brake, a_brake, delta_h, incline, is_downhill, self.was_downhill)

    self.last_delta_height = delta_h
    self.last_incline = incline
    self.was_downhill = is_downhill

    return cruise[self.cruise_plan]
