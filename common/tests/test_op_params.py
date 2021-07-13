import numpy as np
import unittest
import math

from cereal import car, log
from common.numpy_fast import interp, is_multi_iter, find_nearest_index
from common.op_params import opParams, eval_breakpoint_source, interp_multi_bp, INDI_INNER_GAIN_BP_MULTI, INDI_INNER_GAIN_V_MULTI, \
                              INDI_MULTI_BREAKPOINT_SOURCE

def create_car_state(vego=0.):
  CS = car.CarState.new_message()
  CS.vEgo = vego

  return CS

def create_controls_state(desired_steer=0.):
  controls_state = log.ControlsState.new_message()
  controls_state.desiredSteerDeg = desired_steer

  return controls_state

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

    expected = [interp(steer_vego_arr[1], bps[1][i], v[i]) for i in set(idxs)]
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
                      [-11, -10, -7, -6, -5.1, -4, -2 -1e-12, 0, 1e-12, 2, 4, 5.1, 6, 7, 10, 11], # desired steer angle
                      [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39, 39.999999, 40, 41] # vego
                    ]
    source_bp = ['desired_steer_abs', 'vego']

    op.put(INDI_INNER_GAIN_BP_MULTI, bps)
    op.put(INDI_INNER_GAIN_V_MULTI, v)
    op.put(INDI_MULTI_BREAKPOINT_SOURCE, source_bp)

    for i, desired_steer in zip(idxs, steer_vego_arr[0]):
      for vego in steer_vego_arr[1]:
        # print(f'i: {i}, steer: {desired_steer}, vego: {vego}')

        x = eval_breakpoint_source(op.get(INDI_MULTI_BREAKPOINT_SOURCE), create_car_state(vego=vego), create_controls_state(desired_steer=desired_steer))
        # print(f'x: {x}')

        interped = interp_multi_bp(x, op.get(INDI_INNER_GAIN_BP_MULTI), op.get(INDI_INNER_GAIN_V_MULTI))
        # print(f'interped: {interped}')

        # print(f'bp: {bps[1][i]}, v: {v[1]}')
        expected = interp(vego, bps[1][i], v[i])
        np.testing.assert_equal(interped, expected)

  def test_multi_breakpoint_fuzzing(self, check_equality=True, bp_extra=None, bp_expected_extra=None, v_extra=None, v_expected_extra=None):
    idxs = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    bp_args = \
              [
                (0, [[0, 10], [[20, 24], [20, 24, 30]]]), # proper steer and vego breakpoint set
                (0, [[0, 10], [[20, 24]]]), # proper steer set, missing one vego
                (1, [[0, 10], [[20, 24], [20, 24, 30], [10, 20, 24, 30]]]), # proper steer set, extra vego
                (0, [[0, 10], [20, 24]]), # proper steer set, normal vego breakpoints (no set)
                (2, [[0, 10]]), # proper steer set only (no vego)
                (3, [0, 10]), # single breakpoint array, take it as is
                (4, [[0, 10], [[20, 24], [20, 24, 30]], [12]]), # proper steer and vego breakpoint set, extra arg
                (4, [[0, 10], [[20, 24]], [12]]), # proper steer set, missing one vego, extra arg
                (4, [[0, 10], [20, 24], [12]]), # proper steer set, normal vego breakpoints (no set), extra arg
                (5, [[0], [[20, 24], [20, 24, 30]]]), # proper vego set, missing one steer
                (5, [0, [[20, 24], [20, 24, 30]]]), # proper vego set, normal steer breakpoints (no set)
                # (0, [[0, 10, 20, 30 , 40, 50], [[20, 24], [20, 24, 30]]]), # extra steer args, proper vego breakpoint set
                # (3, [[0, 10, 20, 30 , 40, 50], [20, 24, 30]]), # extra steer args, proper vego breakpoint set
                # (6, [[0, 5, 15], [20, 24, 30]]) # steer set causes index overflow when find index is higher than v
                (7, [[0], [0, 4, 7]]),
              ]
    bp_expected = \
                  [
                    [[0, 10], [[20, 24], [20, 24, 30]]],
                    [[0, 10], [[20, 24], [10, 20, 24, 30]]],
                    [[0, 10], [0, 10]],
                    [0, 10],
                    [[0, 10], [[20, 24], [12]]],
                    [[0, 0], [[20, 24], [20, 24, 30]]],
                    [[0, 5, 15], [[20, 24, 30], [20, 24, 30]]],
                    [[0, 0], [0, 4, 7]],
                  ]
    v_args = \
            [
              (0, [[5, 5.75], [6, 7.25, 7.5]]), # proper value set
              (1, [[5, 5.75]]), # value set missing one option
              (2, [6, 7.25, 7.5]), # normal value breakpoint, no set
              (0, [[5, 5.75], [6, 7.25, 7.5], [8, 9]]), # value set with extra arg
              (3, [[7.5, 8.5, 11]]),
              (4, [[0.5, 0.35, 0.3]]),
            ]
    v_expected = \
                [
                  [[5, 5.75], [6, 7.25, 7.5]],
                  [5, 5.75],
                  [6, 7.25, 7.5],
                  [[7.5, 8.5, 11], [7.5, 8.5, 11]],
                  [[0.5, 0.35, 0.3], [0.5, 0.35, 0.3]]
                ]
    steer_vego_arr = \
                    [
                      [-11, -10, -7, -6, -5, -4, -2 -1e-12, 0, 1e-12, 2, 4, 5, 6, 7, 10, 11], # desired steer angle
                      [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39, 39.999999, 40, 41], # vego
                    ]

    if bp_extra:
      bp_args += bp_extra
    if bp_expected_extra:
      bp_expected += bp_expected_extra
    if v_extra:
      v_args += v_extra
    if v_expected_extra:
      v_expected += v_expected_extra

    for bp_i, bps in bp_args:
      # print(f'bps: {bps}')
      if is_multi_iter(bps) and hasattr(bps[0], '__iter__'):
        idxs = find_nearest_index(bps[0], steer_vego_arr[0])

      bps_expct = bp_expected[bp_i if bp_i < len(bp_expected) else 0]

      if is_multi_iter(bps_expct) and not is_multi_iter(bps_expct[-1]):
        bps_expct[-1] = [bps_expct[-1], bps_expct[-1]]

      for v_i, v in v_args:
        v_expct = v_expected[v_i if v_i < len(v_expected) else 0]

        with self.subTest(msg='Fuzzing multi breakpoints bp: bp, v value: v_value', bp=bps, v_value=v):
          interped = interp_multi_bp(steer_vego_arr, bps, v)

          # print(f'interped:\n {interped}')
          # print(f'bps: {bps}')
          # print(f'bps_expected: {bps_expct}')

          expected = [interp(steer_vego_arr[-1],
                      bps_expct[-1][-1] if is_multi_iter(bps_expct) else bps_expct,
                      v_expct[min(len(v_expct) - 1, i)] if is_multi_iter(v_expct) else v_expct)
                      for i in set(idxs)]
          if len(set(idxs)) <= 1:
            expected = expected[0]

          # print(f'expected:\n {expected}')

          if check_equality:
            np.testing.assert_equal(interped, expected)

          for i, desired_steer in zip(idxs, steer_vego_arr[0]):
            for vego in steer_vego_arr[1]:
              # print(f'i: {i}, steer: {desired_steer}, vego: {vego}')

              interped = interp_multi_bp([desired_steer, vego], bps, v)
              # print(f'interped:\n {interped}')

              expected = interp(vego,
                                bps_expct[-1][-1] if is_multi_iter(bps_expct) else bps_expct,
                                v_expct[min(len(v_expct) - 1, i)] if is_multi_iter(v_expct) else v_expct)
              # print(f'expected:\n {expected}')
              if check_equality:
                np.testing.assert_equal(interped, expected)

  def test_multi_breakpoint_fuzzing_error(self):
    bp_args = \
              [
                (0, [[0, 5, 15], [20, 24, 30]]) # steer set causes index overflow when find index is higher than v
              ]
    bp_expected = \
                  [
                    [[0, 5, 15], [[20, 24, 30], [20, 24, 30]]]
                  ]
    v_args = \
            [

            ]
    v_expected = \
                [

                ]

    self.test_multi_breakpoint_fuzzing(check_equality=False, bp_extra=bp_args, bp_expected_extra=bp_expected, v_extra=v_args, v_expected_extra=v_expected)


if __name__ == "__main__":
  unittest.main()
