import numpy as np
import unittest

from cereal import car, log
from common.numpy_fast import interp, is_multi_iter
from common.op_params import opParams, eval_breakpoint_source, interp_multi_bp, INDI_INNER_GAIN_BP_MULTI, INDI_INNER_GAIN_V_MULTI, \
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

  def test_multi_breakpoint_short_steer_bp(self):
    idxs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bps = [[0], [[20, 24], [20, 24, 30]]]
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

    expected = interp(steer_vego_arr[1], bps[1][0], v[0])
    # print(f'expected: {expected}')
    np.testing.assert_equal(interped, expected)

    for i, desired_steer in zip(idxs, steer_vego_arr[0]):
      for vego in steer_vego_arr[1]:
        # print(f'i: {i}, steer: {desired_steer}, vego: {vego}')

        interped = interp_multi_bp([desired_steer, vego], bps, v)
        # print(f'interped: {interped}')

        expected = interp(vego, bps[1][i], v[i])
        np.testing.assert_equal(interped, expected)

  def test_multi_breakpoint_no_steer_bp(self):
    idxs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bps = [[[20, 24], [20, 24, 30]]]
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

    expected = interp(steer_vego_arr[-1], bps[-1][0], v[0])
    # print(f'expected: {expected}')
    np.testing.assert_equal(interped, expected)

    for i, desired_steer in zip(idxs, steer_vego_arr[0]):
      for vego in steer_vego_arr[-1]:
        # print(f'i: {i}, steer: {desired_steer}, vego: {vego}')

        interped = interp_multi_bp([desired_steer, vego], bps, v)
        # print(f'interped: {interped}')

        expected = interp(vego, bps[-1][i], v[i])
        np.testing.assert_equal(interped, expected)

  def test_multi_breakpoint_missing_steer_equivalence(self):
    idxs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bps = [[[20, 24], [20, 24, 30]]]
    v = [[5, 5.75], [6, 7.25, 7.5]]
    steer_vego_arr = \
                    [
                      [-11, -10, -7, -6, -5, -4, -2 -1e-12, 0, 1e-12, 2, 4, 5, 6, 7, 10, 11], # desired steer angle
                      [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39, 39.999999, 40, 41] # vego
                    ]

    expected = interp_multi_bp(steer_vego_arr, bps, v)
    # print(f'expected: {expected}')

    bps.insert(0, [0])
    interped = interp_multi_bp(steer_vego_arr, bps, v)
    # print(f'interped: {interped}')

    np.testing.assert_equal(interped, expected)

    for i, desired_steer in zip(idxs, steer_vego_arr[0]):
      for vego in steer_vego_arr[-1]:
        # print(f'i: {i}, steer: {desired_steer}, vego: {vego}')

        interped = interp_multi_bp([desired_steer, vego], bps, v)
        # print(f'interped: {interped}')

        expected = interp(vego, bps[-1][i], v[i])
        np.testing.assert_equal(interped, expected)

  def test_multi_breakpoint_short_vego_bp(self):
    idxs = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    steer_args = [0, 10]
    v_ego_args = \
                [
                  [[20, 24], [20, 24, 30]], # proper v_ego set
                  [[20, 24]], # v_ego set missing one option
                  [20, 24, 30] # normal v_ego breakpoint, no set
                ]
    bps_expected = [[0, 10], [[20, 24], [20, 24, 30]]]
    v = [[5, 5.75], [6, 7.25, 7.5]]
    steer_vego_arr = \
                    [
                      [-11, -10, -7, -6, -5, -4, -2 -1e-12, 0, 1e-12, 2, 4, 5, 6, 7, 10, 11], # desired steer angle
                      [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39, 39.999999, 40, 41] # vego
                    ]

    for vego in v_ego_args:
      with self.subTest(msg='Testing with short vego: v_ego', v_ego=vego):
        bps = [steer_args, vego]
        interped = interp_multi_bp(steer_vego_arr, bps, v)
        # print(f'interped: {interped}')

        bps = np.asarray(bps, dtype=object)
        v = np.asarray(v, dtype=object)
        steer_vego_arr = np.asarray(steer_vego_arr, dtype=object)

        expected = [interp(steer_vego_arr[1], bps_expected[1][i], v[i]) for i in set(idxs)]
        # print(f'expected: {expected}')
        np.testing.assert_equal(interped, expected)

        for i, desired_steer in zip(idxs, steer_vego_arr[0]):
          for vego in steer_vego_arr[1]:
            # print(f'i: {i}, steer: {desired_steer}, vego: {vego}')

            interped = interp_multi_bp([desired_steer, vego], bps, v)
            # print(f'interped: {interped}')

            expected = interp(vego, bps[1][-1], v[i])
            np.testing.assert_equal(interped, expected)

  def test_multi_breakpoint_short_v(self):
    idxs = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    bps = [[0, 10], [[20, 24], [20, 24, 30]]]
    v_args = \
            [
              [[5, 5.75], [6, 7.25, 7.5]], # proper value set
              [[5, 5.75]], # value set missing one option
              [6, 7.25, 7.5], # normal value breakpoint, no set
            ]
    v_expected = \
                [
                  [[5, 5.75], [6, 7.25, 7.5]],
                  [5, 5.75],
                  [6, 7.25, 7.5],
                ]
    steer_vego_arr = \
                    [
                      [-11, -10, -7, -6, -5, -4, -2 -1e-12, 0, 1e-12, 2, 4, 5, 6, 7, 10, 11], # desired steer angle
                      [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39, 39.999999, 40, 41] # vego
                    ]

    for v_expct, v in zip(v_expected, v_args):
      with self.subTest(msg='Testing with short v value: v_value', v_value=v):
        interped = interp_multi_bp(steer_vego_arr, bps, v)
        # print(f'interped: {interped}')

        expected = [interp(steer_vego_arr[1], bps[1][i], v_expct[i] if is_multi_iter(v_expct) else v_expct) for i in set(idxs)]
        # print(f'expected: {expected}')
        np.testing.assert_equal(interped, expected)

        for i, desired_steer in zip(idxs, steer_vego_arr[0]):
          for vego in steer_vego_arr[1]:
            # print(f'i: {i}, steer: {desired_steer}, vego: {vego}')

            interped = interp_multi_bp([desired_steer, vego], bps, v)
            # print(f'interped: {interped}')

            expected = interp(vego, bps[1][i], v_expct[i] if is_multi_iter(v_expct) else v_expct)
            np.testing.assert_equal(interped, expected)

  def test_multi_breakpoint_fuzzing(self):
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
              ]
    bp_expected = \
                  [
                    [[0, 10], [[20, 24], [20, 24, 30]]],
                    [[0, 10], [[20, 24], [10, 20, 24, 30]]],
                    [[0, 10], [0, 10]],
                    [0, 10],
                    [[0, 10], [[20, 24], [12]]],
                  ]
    v_args = \
            [
              (0, [[5, 5.75], [6, 7.25, 7.5]]), # proper value set
              (1, [[5, 5.75]]), # value set missing one option
              (2, [6, 7.25, 7.5]), # normal value breakpoint, no set
              (0, [[5, 5.75], [6, 7.25, 7.5], [8, 9]]) # value set with extra arg
            ]
    v_expected = \
                [
                  [[5, 5.75], [6, 7.25, 7.5]],
                  [5, 5.75],
                  [6, 7.25, 7.5],
                ]
    steer_vego_arr = \
                    [
                      [-11, -10, -7, -6, -5, -4, -2 -1e-12, 0, 1e-12, 2, 4, 5, 6, 7, 10, 11], # desired steer angle
                      [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39, 39.999999, 40, 41] # vego
                    ]
    for bp_i, bps in bp_args:
      # print(f'bps: {bps}')
      bps_expct = bp_expected[bp_i if bp_i < len(bp_expected) else 0]

      if is_multi_iter(bps_expct) and not is_multi_iter(bps_expct[-1]):
        bps_expct[-1] = [bps_expct[-1], bps_expct[-1]]

      for v_i, v in v_args:
        v_expct = v_expected[v_i if v_i < len(v_expected) else 0]

        with self.subTest(msg='Fuzzing multi breakpoints bp: bp, v value: v_value', bp=bps, v_value=v):
          interped = interp_multi_bp(steer_vego_arr, bps, v)

          # print(f'interped: {interped}')
          # print(f'bps: {bps}')
          # print(f'bps_expected: {bps_expct}')

          expected = [interp(steer_vego_arr[-1],
                      bps_expct[-1][-1] if is_multi_iter(bps_expct) else bps_expct,
                      v_expct[i] if is_multi_iter(v_expct) else v_expct)
                      for i in set(idxs)]
          # print(f'expected: {expected}')

          np.testing.assert_equal(interped, expected)

          for i, desired_steer in zip(idxs, steer_vego_arr[0]):
            for vego in steer_vego_arr[1]:
              # print(f'i: {i}, steer: {desired_steer}, vego: {vego}')

              interped = interp_multi_bp([desired_steer, vego], bps, v)
              # print(f'interped: {interped}')

              expected = interp(vego,
                                bps_expct[-1][-1] if is_multi_iter(bps_expct) else bps_expct,
                                v_expct[i] if is_multi_iter(v_expct) else v_expct)
              np.testing.assert_equal(interped, expected)


if __name__ == "__main__":
  unittest.main()
