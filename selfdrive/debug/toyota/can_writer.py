#!/usr/bin/env python3
from time import sleep

import cereal.messaging as messaging
from cereal.services import service_list
from opendbc.can.packer import CANPacker
from common.op_params import opParams, ENABLE_AUTO_HIGH_BEAMS, CAN_WRITE_LIGHT_STALK, \
                            CAN_LIGHT_STALK_AUTO_HB, CAN_LIGHT_STALK_AUTO_HB_ON, \
                            CAN_LIGHT_STALK_AUTO_LIGHTS, CAN_LIGHT_STALK_HB_ON, \
                            CAN_LIGHT_STALK_LB_ON, CAN_LIGHT_STALK_TRANSITION, \
                            CAN_LIGHT_STALK_DASH_ICON, CAN_LIGHT_STALK_SLEEP
from selfdrive.car.toyota.toyotacan import create_high_beam_command
from selfdrive.boardd.boardd import can_list_to_can_capnp



def main():
  packer = CANPacker()
  op_params = opParams()
  sendcan = messaging.pub_sock(service_list['sendcan'].port)

  while True:
    if op_params.get(ENABLE_AUTO_HIGH_BEAMS) and op_params.get(CAN_WRITE_LIGHT_STALK):
      cmd = create_high_beam_command(packer, op_params.get(CAN_LIGHT_STALK_HB_ON), op_params.get(CAN_LIGHT_STALK_LB_ON),
                              op_params.get(CAN_LIGHT_STALK_AUTO_LIGHTS), op_params.get(CAN_LIGHT_STALK_TRANSITION),
                              op_params.get(CAN_LIGHT_STALK_AUTO_HB), op_params.get(CAN_LIGHT_STALK_DASH_ICON),
                              op_params.get(CAN_LIGHT_STALK_AUTO_HB_ON))
      sendcan.send(can_list_to_can_capnp([cmd], msgtype='sendcan'))
      sleep(op_params.get(CAN_LIGHT_STALK_SLEEP))



if __name__ == "__main__":
    main()
