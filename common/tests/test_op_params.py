import numpy as np
import unittest

from common.numpy_fast import interp
from common.op_params import opParams


class OpParamsTest(unittest.TestCase):
  def test_correctness_multi_breakpoint(self):
    op_params = opParams()
    bps = [[0, 10], [[20, 24], [20, 24, 30]]]
    v = [[5, 5.75], [6, 7.25, 7.5]]
    steer_vego_arr = [[-1, -1e-12, 0, 4, 5, 6, 7, 10, 11], [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39,
                 39.999999, 40, 41]]
    # Todo: write function to interp bp args    
    actual = interp(steer_vego_arr, bps, v)
    print(f'actual: {actual}')

    for v_ego in steer_vego_arr:
      actual = interp(v_ego, bps, v)
      print(f'actual: {actual}')

if __name__ == "__main__":
  unittest.main()