def create_steer_command(packer, steer, steer_req, raw_cnt):
  """Creates a CAN message for the Toyota Steer Command."""

  values = {
    "STEER_REQUEST": steer_req,
    "STEER_TORQUE_CMD": steer,
    "COUNTER": raw_cnt,
    "SET_ME_1": 1,
  }
  return packer.make_can_msg("STEERING_LKA", 0, values)


def create_lta_steer_command(packer, steer, steer_req, raw_cnt):
  """Creates a CAN message for the Toyota LTA Steer Command."""

  values = {
    "COUNTER": raw_cnt + 128,
    "SETME_X1": 1,
    "SETME_X3": 3,
    "PERCENTAGE": 100,
    "SETME_X64": 0x64,
    "ANGLE": 0,  # Rate limit? Lower values seeem to work better, but needs more testing
    "STEER_ANGLE_CMD": steer,
    "STEER_REQUEST": steer_req,
    "STEER_REQUEST_2": steer_req,
    "BIT": 0,
  }
  return packer.make_can_msg("STEERING_LTA", 0, values)


def create_accel_command(packer, accel, pcm_cancel, standstill_req, lead, acc_type=1, permit_braking=1):
  # TODO: find the exact canceling bit that does not create a chime
  values = {
    "ACCEL_CMD": accel,
    "SET_ME_X01": acc_type,
    "DISTANCE": 0,
    "MINI_CAR": lead,
    "SET_ME_X3": 3,
    "PERMIT_BRAKING": permit_braking,
    "RELEASE_STANDSTILL": not standstill_req,
    "CANCEL_REQ": pcm_cancel,
  }
  return packer.make_can_msg("ACC_CONTROL", 0, values)


def create_acc_cancel_command(packer):
  values = {
    "GAS_RELEASED": 0,
    "CRUISE_ACTIVE": 0,
    "STANDSTILL_ON": 0,
    "ACCEL_NET": 0,
    "CRUISE_STATE": 0,
    "CANCEL_REQ": 1,
  }
  return packer.make_can_msg("PCM_CRUISE", 0, values)


def create_fcw_command(packer, fcw):
  values = {
    "FCW": fcw,
    "SET_ME_X20": 0x20,
    "SET_ME_X10": 0x10,
    "SET_ME_X80": 0x80,
  }
  return packer.make_can_msg("ACC_HUD", 0, values)


def create_ui_command(packer, steer, chime, left_line, right_line, left_lane_depart, right_lane_depart):
  values = {
    "RIGHT_LINE": 3 if right_lane_depart else 1 if right_line else 2,
    "LEFT_LINE": 3 if left_lane_depart else 1 if left_line else 2,
    "BARRIERS" : 3 if left_lane_depart else 2 if right_lane_depart else 0,
    "SET_ME_X0C": 0x0c,
    "SET_ME_X2C": 0x2c,
    "SET_ME_X38": 0x38,
    "SET_ME_X02": 0x02,
    "SET_ME_X01": 1,
    "SET_ME_X01_2": 1,
    "REPEATED_BEEPS": 0,
    "TWO_BEEPS": chime,
    "LDA_ALERT": steer,
  }
  return packer.make_can_msg("LKAS_HUD", 0, values)

def create_high_beam_command(packer, high_beam, low_beam_on=1, auto_lights=1, transition=1, auto_hb=1, dash_icon=1, auto_hb_on=1):
  values = {
    "SET_ME_X12": 0x12,
    "HIGH_BEAM_ON": 1 if high_beam else 0,
    "LOW_BEAM_ON": low_beam_on,
    "AUTO_LIGHTS": auto_lights,
    "STATE_TRANSITION": transition,
    "AUTO_HIGH_BEAM": auto_hb,
    "DASH_ICON": dash_icon,
    "AUTO_HIGH_BEAM_ON" : auto_hb_on,
  }
  return packer.make_can_msg("LIGHT_STALK", 0, values)
