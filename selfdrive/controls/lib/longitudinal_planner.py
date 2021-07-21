#!/usr/bin/env python3
import math
import numpy as np
from common.numpy_fast import interp

import cereal.messaging as messaging
from cereal import log
from common.realtime import DT_MDL
from common.realtime import sec_since_boot
from common.op_params import opParams, ENABLE_PLANNER_PARAMS, ENABLE_PLNR_ACCEL_LIMITS
from selfdrive.modeld.constants import T_IDXS
from selfdrive.config import Conversions as CV
from selfdrive.controls.lib.fcw import FCWChecker
from selfdrive.controls.lib.longcontrol import LongCtrlState
from selfdrive.controls.lib.lead_mpc import LeadMpc
from selfdrive.controls.lib.long_mpc import LongitudinalMpc
from selfdrive.controls.lib.drive_helpers import V_CRUISE_MAX, CONTROL_N
from selfdrive.swaglog import cloudlog

LON_MPC_STEP = 0.2  # first step is 0.2s
AWARENESS_DECEL = -0.2     # car smoothly decel at .2m/s^2 when user is distracted
A_CRUISE_MIN = -1.2
A_CRUISE_MAX = 1.2

# Lookup table for turns
_A_TOTAL_MAX_V = [1.7, 3.2]
_A_TOTAL_MAX_BP = [20., 40.]

Source = log.LongitudinalPlan.LongitudinalPlanSource


def calc_cruise_accel_limits(v_ego, following, op_params):
  if op_params.get(ENABLE_PLANNER_PARAMS) and op_params.get(ENABLE_PLNR_ACCEL_LIMITS):
    min_key = "a_cruise_min_v"
    max_key = "a_cruise_max_v"

    if following:
      min_key += "_following"
      max_key += "_following"

    min_bp = op_params.get('a_cruise_min_bp')
    min_v = op_params.get(min_key)
    max_bp = op_params.get('a_cruise_max_bp')
    max_v = op_params.get(max_key)

    return [interp(v_ego, min_bp, min_v), interp(v_ego, max_bp, max_v)]
  else:
    return [A_CRUISE_MIN, A_CRUISE_MAX]


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
    self.mpcs = {}
    self.mpcs['lead0'] = LeadMpc(0)
    self.mpcs['lead1'] = LeadMpc(1)
    self.mpcs['cruise'] = LongitudinalMpc()

    self.fcw = False
    self.fcw_checker = FCWChecker()

    self.v_desired = 0.0
    self.a_desired = 0.0
    self.longitudinalPlanSource = Source.cruiseGas
    self.cruise_plan = Source.cruiseGas
    self.alpha = np.exp(-DT_MDL/2.0)
    self.lead_0 = log.ModelDataV2.LeadDataV3.new_message()
    self.lead_1 = log.ModelDataV2.LeadDataV3.new_message()

    self.v_desired_trajectory = np.zeros(CONTROL_N)
    self.a_desired_trajectory = np.zeros(CONTROL_N)

    if OP is None:
      OP = opParams()

    self.op_params = OP

    self.avg_height = 0.0 # Average distance from the camera to the ground in meters
    self.height_samples = 0
    self.last_delta_height = 0.0

    self.last_incline = 0.0 # Last incline of the road in radians
    self.was_downhill = False


  def update(self, sm, CP):
    cur_time = sec_since_boot()
    v_ego = sm['carState'].vEgo
    a_ego = sm['carState'].aEgo

    v_cruise_kph = sm['controlsState'].vCruise
    v_cruise_kph = min(v_cruise_kph, V_CRUISE_MAX)
    v_cruise = v_cruise_kph * CV.KPH_TO_MS

    long_control_state = sm['controlsState'].longControlState
    force_slow_decel = sm['controlsState'].forceDecel

    self.lead_0 = sm['radarState'].leadOne
    self.lead_1 = sm['radarState'].leadTwo

    enabled = (long_control_state == LongCtrlState.pid) or (long_control_state == LongCtrlState.stopping)
    following = self.lead_1.status and self.lead_1.dRel < 45.0 and self.lead_1.vLeadK > v_ego and self.lead_1.aLeadK > 0.0

    if not enabled or sm['carState'].gasPressed:
      self.v_desired = v_ego
      self.a_desired = a_ego

    # Prevent divergence, smooth in current v_ego
    self.v_desired = self.alpha * self.v_desired + (1 - self.alpha) * v_ego
    self.v_desired = max(0.0, self.v_desired)

    accel_limits = calc_cruise_accel_limits(v_ego, following, self.op_params)
    accel_limits_turns = limit_accel_in_turns(v_ego, sm['carState'].steeringAngleDeg, accel_limits, self.CP)
    if force_slow_decel:
      # if required so, force a smooth deceleration
      accel_limits_turns[1] = min(accel_limits_turns[1], AWARENESS_DECEL)
      accel_limits_turns[0] = min(accel_limits_turns[0], accel_limits_turns[1])
    # clip limits, cannot init MPC outside of bounds
    accel_limits_turns[0] = min(accel_limits_turns[0], self.a_desired)
    accel_limits_turns[1] = max(accel_limits_turns[1], self.a_desired)
    self.mpcs['cruise'].set_accel_limits(accel_limits_turns[0], accel_limits_turns[1])

    next_a = np.inf
    for key in self.mpcs:
      self.mpcs[key].set_cur_state(self.v_desired, self.a_desired)
      self.mpcs[key].update(sm['carState'], sm['radarState'], v_cruise)
      if self.mpcs[key].status and self.mpcs[key].a_solution[5] < next_a:
        self.longitudinalPlanSource = key
        self.v_desired_trajectory = self.mpcs[key].v_solution[:CONTROL_N]
        self.a_desired_trajectory = self.mpcs[key].a_solution[:CONTROL_N]
        next_a = self.mpcs[key].a_solution[5]

    # determine fcw
    if self.mpcs['lead0'].new_lead:
      self.fcw_checker.reset_lead(cur_time)
    blinkers = sm['carState'].leftBlinker or sm['carState'].rightBlinker
    self.fcw = self.fcw_checker.update(self.mpcs['lead0'].mpc_solution, cur_time,
                                       sm['controlsState'].active,
                                       v_ego, sm['carState'].aEgo,
                                       self.lead_1.dRel, self.lead_1.vLead, self.lead_1.aLeadK,
                                       self.lead_1.yRel, self.lead_1.vLat,
                                       self.lead_1.fcw, blinkers) and not sm['carState'].brakePressed
    if self.fcw:
      cloudlog.info("FCW triggered %s", self.fcw_checker.counters)

    # Interpolate 0.05 seconds and save as starting point for next iteration
    a_prev = self.a_desired
    self.a_desired = np.interp(DT_MDL, T_IDXS[:CONTROL_N], self.a_desired_trajectory)
    self.v_desired = self.v_desired + DT_MDL * (self.a_desired + a_prev)/2.0

  def publish(self, sm, pm):
    plan_send = messaging.new_message('longitudinalPlan')

    plan_send.valid = sm.all_alive_and_valid(service_list=['carState', 'controlsState'])

    longitudinalPlan = plan_send.longitudinalPlan
    longitudinalPlan.modelMonoTime = sm.logMonoTime['modelV2']
    longitudinalPlan.processingDelay = (plan_send.logMonoTime / 1e9) - sm.logMonoTime['modelV2']

    longitudinalPlan.speeds = [float(x) for x in self.v_desired_trajectory]
    longitudinalPlan.accels = [float(x) for x in self.a_desired_trajectory]

    longitudinalPlan.hasLead = self.mpcs['lead0'].status
    longitudinalPlan.longitudinalPlanSource = self.longitudinalPlanSource
    longitudinalPlan.fcw = self.fcw

    pm.send('longitudinalPlan', plan_send)

  # This needs to be rethought so I'm not gonna bother updating it for current OP changes
  # def choose_cruise(self, sm, v_ego, a_ego, v_cruise_setpoint, accel_limits_turns, jerk_limits):
  #   delta_h = self.last_delta_height
  #   incline = self.last_incline

  #   # Use the new depth net to calculate the incline of the road
  #   if sm.updated['modelV2']:
  #     md = sm['modelV2']

  #     if len(md.laneLines):
  #       # Get the hights of the camera at each time step from each lane line
  #       heights = np.array([ll.z for ll in md.laneLines])
  #       # Collapse heights into a 1D array containing the average height at each time step
  #       # weighted by the model's confidence in its lane predicitions
  #       heights = np.average(heights, axis=0, weights=md.laneLineProbs)

  #       # x and t are always the same for all lanes so just grab the first one
  #       steps = md.laneLines[0].t

  #       # Get the average forward and heights changes
  #       # weighted by time since we're planning for the future
  #       delta_x = np.average(md.laneLines[0].x, weights=steps)
  #       delta_h = np.average(heights, weights=steps)

  #       # Get the average distance from the camera to the road throughout the drive
  #       self.height_samples +=1
  #       self.avg_height = incremental_avg(self.avg_height, heights[0], self.height_samples)

  #       # Get the angle, in radians, between the average and future height of the camera
  #       # Negate because a positive angle means we're going downhill
  #       incline = -math.atan2(delta_h - self.avg_height, delta_x)

  #   # When coasting, reset plans
  #   if self.longitudinalPlanSource == Source.cruiseCoast:
  #     self.v_acc_start = v_ego
  #     self.a_acc_start = a_ego

  #   # When following return to cruiseGas
  #   if self.longitudinalPlanSource in [Source.mpc1, Source.mpc2]:
  #     self.cruise_plan = Source.cruiseGas

  #   # Coast continues current state
  #   v_coast, a_coast = v_ego + a_ego * LON_MPC_STEP, a_ego
  #   cruise = {Source.cruiseCoast: (v_coast, a_coast)}

  #   # Gas to v_cruise_setpoint
  #   v_gas, a_gas = speed_smoother(self.v_acc_start, self.a_acc_start,
  #                                 v_cruise_setpoint,
  #                                 accel_limits_turns[1], accel_limits_turns[0],
  #                                 jerk_limits[1], jerk_limits[0],
  #                                 LON_MPC_STEP)

  #   cruise[Source.cruiseGas] = (v_gas, a_gas)

  #   coast_setpoint = v_cruise_setpoint + self.coast_speed
  #   # Brake to (v_cruise_setpoint + COAST_SPEED)
  #   # TODO: rethink this for toyota? v_cruise_setpoint has to be lower than
  #   # the car's setpoint or the car will engine brake on its own.
  #   # In other words the max speed (with coasting) is the car's setpoint.
  #   v_brake, a_brake = speed_smoother(self.v_acc_start, self.a_acc_start,
  #                                     coast_setpoint,
  #                                     accel_limits_turns[1], accel_limits_turns[0],
  #                                     jerk_limits[1], jerk_limits[0],
  #                                     LON_MPC_STEP)

  #   cruise[Source.cruiseBrake] = (v_brake, a_brake)

  #   dh_incline = math.radians(self.op_params.get(DOWNHILL_INCLINE))
  #   is_downhill = incline < dh_incline or v_ego > v_cruise_setpoint

  #   # Entry conditions
  #   if self.op_params.get(ALWAYS_EVAL_COAST) or is_downhill or is_downhill != self.was_downhill:
  #     if is_downhill:
  #       self.cruise_plan = Source.cruiseCoast if v_ego < coast_setpoint else Source.cruiseBrake
  #     else:
  #       self.cruise_plan = Source.cruiseGas

  #   cloudlog.info("Cruise Plan %s: ego(%f,%f) gas(%f,%f) coast(%f,%f) brake(%f,%f) delta_h(%f) incline(%f) is_downhill(%s) was_downhill(%s)",
  #                 self.cruise_plan, v_ego, a_ego, v_gas, a_gas, v_coast, a_coast,
  #                 v_brake, a_brake, delta_h, incline, is_downhill, self.was_downhill)

  #   self.last_delta_height = delta_h
  #   self.last_incline = incline
  #   self.was_downhill = is_downhill

  #   return cruise[self.cruise_plan]
