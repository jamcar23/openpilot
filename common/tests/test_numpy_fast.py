import numpy as np
import unittest

from common.numpy_fast import interp, interp_2d
from common.op_params import interp_multi_bp


class InterpTest(unittest.TestCase):
  def test_correctness_controls(self):
    _A_CRUISE_MIN_BP = np.asarray([0., 5., 10., 20., 40.])
    _A_CRUISE_MIN_V = np.asarray([-1.0, -.8, -.67, -.5, -.30])
    v_ego_arr = [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39,
                 39.999999, 40, 41]

    expected = np.interp(v_ego_arr, _A_CRUISE_MIN_BP, _A_CRUISE_MIN_V)
    actual = interp(v_ego_arr, _A_CRUISE_MIN_BP, _A_CRUISE_MIN_V)

    np.testing.assert_equal(actual, expected)

    for v_ego in v_ego_arr:
      expected = np.interp(v_ego, _A_CRUISE_MIN_BP, _A_CRUISE_MIN_V)
      actual = interp(v_ego, _A_CRUISE_MIN_BP, _A_CRUISE_MIN_V)
      np.testing.assert_equal(actual, expected)

  def test_short_bp_long_v(self):
    bp_test_cases = ([0], [0, 5], [0., 5., 10.], [0., 5., 10., 20], [-1., 2., 13., 16])
    bp_expected_cases = ([0, 0, 0, 0, 0], [0, 5, 5, 5, 5], [0., 5., 10., 10., 10.], [0., 5., 10., 20., 20.], [-1., 2., 13., 16, 16.])
    _A_CRUISE_MIN_V = np.asarray([-1.0, -.8, -.67, -.5, -.30])
    v_ego_arr = [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39,
                 39.999999, 40, 41]

    for bp_a, bp_e in zip(bp_test_cases, bp_expected_cases):
      with self.subTest(msg='Checking if bp_a equals bp_e', bp_a=bp_a, bp_e=bp_e):
        expected = np.interp(v_ego_arr, bp_e, _A_CRUISE_MIN_V)
        actual = interp(v_ego_arr, bp_a, _A_CRUISE_MIN_V)

        np.testing.assert_equal(actual, expected)

        for v_ego in v_ego_arr:
          expected = np.interp(v_ego, bp_e, _A_CRUISE_MIN_V)
          actual = interp(v_ego, bp_a, _A_CRUISE_MIN_V)
          np.testing.assert_equal(actual, expected)

  def test_long_bp_short_v(self):
    _A_CRUISE_MIN_BP = np.asarray([0., 5., 10., 20., 40.])
    v_test_cases = ([-1.0], [-1.0, -.8], [-1.0, -.8, -.67], [-1.0, -.8, -.67, -.5])
    v_expected_cases = ([-1.0, -1., -1., -1., -1.], [-1.0, -.8, -.8, -.8, -.8], [-1.0, -.8, -.67, -.67, -.67], [-1.0, -.8, -.67, -.5, -.5])
    v_ego_arr = [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39,
                 39.999999, 40, 41]

    for v_a, v_e in zip(v_test_cases, v_expected_cases):
      with self.subTest(msg='Checking if v_a equals v_e', v_a=v_a, v_e=v_e):
        expected = np.interp(v_ego_arr, _A_CRUISE_MIN_BP, v_e)
        actual = interp(v_ego_arr, _A_CRUISE_MIN_BP, v_a)
        np.testing.assert_equal(actual, expected)

        for v_ego in v_ego_arr:
          expected = np.interp(v_ego, _A_CRUISE_MIN_BP, v_e)
          actual = interp(v_ego, _A_CRUISE_MIN_BP, v_a)
          np.testing.assert_equal(actual, expected)

  def test_correctness_controls_2d(self):
    bps = [[0, 10], [20, 24, 30]]
    v = [[5, 5.75], [7.25, 7.5]]
    steer_vego_arr = \
                    [
                      [-11, -10, -7, -6, -5, -4, -2 -1e-12, 0, 1e-12, 2, 4, 5, 7, 10, 11], # desired steer angle
                      [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39, 39.999999, 40, 41] # vego
                    ]
    expected = [5, 5, 5, 5, 5, 5, 5, 5, 5.000000000000225, 5.45, 5.9, 6.25, 6.975, 7.5, 7.5, 7.5]


    actual = interp_2d(steer_vego_arr, bps, v)
    # print(f'actual: {actual}')
    # print(f'interped: {interp_multi_bp(steer_vego_arr, bps, v)}')
    # np.interp(steer_vego_arr, bps, v)
    np.testing.assert_equal(actual, expected)

    # i = 0
    for desired_steer in steer_vego_arr[0]:
      for v_ego in steer_vego_arr[1]:
        x = [desired_steer, v_ego]
        actual = interp_2d(x, bps, v)
        # print(f'actual: {actual}')
        # print(f'expected: {expected}')
        # assert actual in expected, f'Actual value not in expected values:\nActual: {actual}\nX: {x}'
        assert not hasattr(actual, '__iter__'), f'Actual should not be an iter:\nActual: {actual}'
        # np.testing.assert_equal(actual, expected[i])
        # i += 1

  # def test_interp_2d_fuzzing(self):
  #   bp_args = \
  #             [
  #               [0, 10],
  #               [[0, 10], [0]]
  #             ]
  #   v_args = \
  #           [
  #             [5, 5.75],
  #           ]
  #   x_args = \
  #             [
  #               [
  #                 [-11, -10, -7, -6, -5, -4, -2 -1e-12, 0, 1e-12, 2, 4, 5, 6, 7, 10, 11], # desired steer angle
  #                 [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39, 39.999999, 40, 41] # vego
  #               ],
  #             ]

  #   for bp in bp_args:
  #     for v in v_args:
  #       for x in x_args:
  #         out = interp_2d(x, bp, v)
  #         assert out

if __name__ == "__main__":
  unittest.main()
