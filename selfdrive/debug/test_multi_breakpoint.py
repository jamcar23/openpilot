#!/usr/bin/env python3

import numpy as np

from common.numpy_fast import interp, find_nearest_index


def interp_multi_bp(x, bp, v):
  idx = find_nearest_index(bp[0], x[0])
  print(f'indexes: {idx}')

  return [interp(x[1], bp[1][i], v[i]) for i in set(idx)] if hasattr(idx, '__iter__') else interp(x[1], bp[1][idx], v[idx])
  # return interp(x[1], bp[1][idx], v[idx])

def main():
  bps = [[0, 10], [[20, 24], [20, 24, 30]]]
  v = [[5, 5.75], [6, 7.25, 7.5]]
  steer_vego_arr = [[-1, -1e-12, 0, 4, 5, 6, 7, 10, 11], [-1, -1e-12, 0, 4, 5, 6, 7, 10, 11, 15.2, 20, 21, 39,
                39.999999, 40, 41]]

  interped = interp_multi_bp(steer_vego_arr, bps, v)
  print(f'interped: {interped}')

  bps = np.asarray(bps, dtype=object)
  v = np.asarray(v, dtype=object)
  steer_vego_arr = np.asarray(steer_vego_arr, dtype=object)

  expected = [interp(steer_vego_arr[1], bps[1][i], v[i]) for i in [0, 1]]
  print(f'expected: {expected}')
  np.testing.assert_equal(interped, expected)


if __name__ == "__main__":
    main()
