import numpy as np
import unittest

from common.numpy_fast import interp


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
    _A_CRUISE_MIN_BP = np.asarray([0., 5., 10.])
    _A_CRUISE_MIN_BP_EXPECTED = np.asarray([0., 5., 10., 10., 10.])
    _A_CRUISE_MIN_V = np.asarray([-1.0, -.8, -.67, -.5, -.30])
    v_ego_arr = [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39,
                 39.999999, 40, 41]

    expected = np.interp(v_ego_arr, _A_CRUISE_MIN_BP_EXPECTED, _A_CRUISE_MIN_V)
    actual = interp(v_ego_arr, _A_CRUISE_MIN_BP, _A_CRUISE_MIN_V)

    np.testing.assert_equal(actual, expected)

    i = 0
    for v_ego in v_ego_arr:
      expected = np.interp(v_ego, _A_CRUISE_MIN_BP_EXPECTED, _A_CRUISE_MIN_V)
      actual = interp(v_ego, _A_CRUISE_MIN_BP, _A_CRUISE_MIN_V)
      np.testing.assert_equal(actual, expected)
      i += 1
  
  def test_long_bp_short_v(self):
    _A_CRUISE_MIN_BP = np.asarray([0., 5., 10., 20., 40.])
    _A_CRUISE_MIN_V = np.asarray([-1.0, -.8, -.67])
    _A_CRUISE_MIN_V_EXPECTED = np.asarray([-1.0, -.8, -.67, -.67, -.67])
    v_ego_arr = [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39,
                 39.999999, 40, 41]

    expected = np.interp(v_ego_arr, _A_CRUISE_MIN_BP, _A_CRUISE_MIN_V_EXPECTED)
    actual = interp(v_ego_arr, _A_CRUISE_MIN_BP, _A_CRUISE_MIN_V)
    np.testing.assert_equal(actual, expected)

    i = 0
    for v_ego in v_ego_arr:
      expected = np.interp(v_ego, _A_CRUISE_MIN_BP, _A_CRUISE_MIN_V_EXPECTED)
      actual = interp(v_ego, _A_CRUISE_MIN_BP, _A_CRUISE_MIN_V)
      np.testing.assert_equal(actual, expected)
      i += 1


if __name__ == "__main__":
  unittest.main()
