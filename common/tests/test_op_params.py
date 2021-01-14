import numpy as np
import unittest

from cereal import car, log
from common.numpy_fast import interp
from selfdrive.debug.test_multi_breakpoint import interp_multi_bp
from common.op_params import opParams, eval_breakpoint_source, INDI_INNER_GAIN_BP_MULTI, INDI_INNER_GAIN_V_MULTI, \
                              INDI_MULTI_BREAKPOINT_SOURCE

def create_car_state(vego=0.):
  CS = car.CarState.new_message()
  CS.vEgo = vego

  return CS

def create_path_plan(desired_steer=0.):
  path_plan = log.PathPlan.new_message()
  path_plan.angleSteers = desired_steer

  return path_plan

class OpParamsTest(unittest.TestCase):
  def test_correctness_multi_breakpoint(self):
    idxs = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    bps = [[0, 10], [[20, 24], [20, 24, 30]]]
    v = [[5, 5.75], [6, 7.25, 7.5]]
    steer_vego_arr = \
                    [
                      [-11, -10, -7, -6, -5, -4, -2 -1e-12, 0, 1e-12, 2, 4, 5, 6, 7, 10, 11], # desired steer angle
                      [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39, 39.999999, 40, 41] # vego
                    ]

    interped = interp_multi_bp(steer_vego_arr, bps, v)
    # print(f'interped: {interped}')

    bps = np.asarray(bps, dtype=object)
    v = np.asarray(v, dtype=object)
    steer_vego_arr = np.asarray(steer_vego_arr, dtype=object)

    expected = [interp(steer_vego_arr[1], bps[1][i], v[i]) for i in [0, 1]]
    # print(f'expected: {expected}')
    np.testing.assert_equal(interped, expected)

    for i, desired_steer in zip(idxs, steer_vego_arr[0]):
      for vego in steer_vego_arr[1]:
        # print(f'i: {i}, steer: {desired_steer}, vego: {vego}')

        interped = interp_multi_bp([desired_steer, vego], bps, v)
        # print(f'interped: {interped}')

        expected = interp(vego, bps[1][i], v[i])
        np.testing.assert_equal(interped, expected)

  def test_correctness_eval_breakpoint_source(self):
    op = opParams()
    idxs = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    bps = [[0, 10], [[20, 24], [20, 24, 30]]]
    v = [[5, 5.75], [6, 7.25, 7.5]]
    steer_vego_arr = \
                    [
                      [-11, -10, -7, -6, -5, -4, -2 -1e-12, 0, 1e-12, 2, 4, 5, 6, 7, 10, 11], # desired steer angle
                      [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39, 39.999999, 40, 41] # vego
                    ]
    source_bp = ['desired_steer_abs', 'vego']

    op.put(INDI_INNER_GAIN_BP_MULTI, bps)
    op.put(INDI_INNER_GAIN_V_MULTI, v)
    op.put(INDI_MULTI_BREAKPOINT_SOURCE, source_bp)

    for i, desired_steer in zip(idxs, steer_vego_arr[0]):
      for vego in steer_vego_arr[1]:
        # print(f'i: {i}, steer: {desired_steer}, vego: {vego}')

        x = eval_breakpoint_source(op.get(INDI_MULTI_BREAKPOINT_SOURCE), create_car_state(vego=vego), create_path_plan(desired_steer=desired_steer))
        # print(f'x: {x}')

        interped = interp_multi_bp(x, op.get(INDI_INNER_GAIN_BP_MULTI), op.get(INDI_INNER_GAIN_V_MULTI))
        # print(f'interped: {interped}')

        expected = interp(vego, bps[1][i], v[i])
        np.testing.assert_equal(interped, expected)

if __name__ == "__main__":
  unittest.main()
