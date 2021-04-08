#!/usr/bin/env python3
from cereal import car
from common.params import Params
from common.realtime import Priority, config_realtime_process
from common.op_params import opParams
from selfdrive.swaglog import cloudlog
from selfdrive.controls.lib.longitudinal_planner import Planner
from selfdrive.controls.lib.lateral_planner import LateralPlanner
from selfdrive.hardware import TICI
import cereal.messaging as messaging


def plannerd_thread(sm=None, pm=None):

  config_realtime_process(2, Priority.CTRL_LOW)

  cloudlog.info("plannerd is waiting for CarParams")
  params = Params()
  CP = car.CarParams.from_bytes(params.get("CarParams", block=True))
  use_lanelines = not params.get_bool('EndToEndToggle')
  wide_camera = (params.get('EnableWideCamera') == b'1') if TICI else False
  cloudlog.info("plannerd got CarParams: %s", CP.carName)

  OP = opParams()
  longitudinal_planner = Planner(CP, OP=OP)
  lateral_planner = LateralPlanner(CP, use_lanelines=use_lanelines, wide_camera=wide_camera, OP=OP)

  if sm is None:
    sm = messaging.SubMaster(['carState', 'controlsState', 'radarState', 'modelV2'],
                             poll=['radarState', 'modelV2'])

  if pm is None:
    pm = messaging.PubMaster(['longitudinalPlan', 'liveLongitudinalMpc', 'lateralPlan', 'liveMpc'])

  while True:
    sm.update()

    if sm.updated['modelV2']:
      lateral_planner.update(sm, CP)
      lateral_planner.publish(sm, pm)
    if sm.updated['radarState']:
      longitudinal_planner.update(sm, CP)
      longitudinal_planner.publish(sm, pm)


def main(sm=None, pm=None):
  plannerd_thread(sm, pm)


if __name__ == "__main__":
  main()
