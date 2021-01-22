import sys

def int_rnd(x):
  return int(round(x))

def clip(x, lo, hi):
  return max(lo, min(hi, x))

def interp(x, xp, fp):
  N = len(xp)
  T = len(fp)

  def get_interp(xv):
    hi = 0
    while hi < N and xv > xp[hi]:
      hi += 1
    low = hi - 1
    return fp[-1] if hi >= T or low >= T or (hi >= N and xv >= xp[low]) or (N < T and xv == xp[-1]) else (
      fp[0] if hi == 0 else
      (xv - xp[low]) * (fp[hi] - fp[low]) / (xp[hi] - xp[low]) + fp[low])

  return [get_interp(v) for v in x] if hasattr(x, '__iter__') else get_interp(x)

def interp_2d(x, y, bp, v):
  N_x = len(bp[0])
  N_y = len(bp[1])

  def get_interp(xv, yv):
    hi_x = 0
    hi_y = 0
    while hi_x < N_x and xv > bp[0][hi_x]:  # get hi for x bp
      hi_x += 1
    while hi_y < N_y and yv > bp[1][hi_y]:  # then get hi for y bp
      hi_y += 1
    low_x = hi_x - 1
    low_y = hi_y - 1

    if ((hi_x == N_x or hi_y == N_y) and xv > bp[0][low_x] and yv > bp[1][low_y]) or hi_x == 0 or hi_y == 0:
      # This branch is taken if either x or y is at top or bottom of their respective BPs
      if hi_x == N_x and hi_y == N_y:  # both top
        return v[-1][-1]
      elif hi_x == 0 and hi_y == 0:  # both bottom
        return v[0][0]
      # Since we know either x or y is at top or bottom we figure out which is what and then just do one interpolation
      # (These two variables use the same if check, it's not as complicated as it looks; this is just shorthand)
      bp_idx = 1 if hi_x in [N_x, 0] else 0
      new_v = v[-1 if hi_x == N_x else 0] if hi_x in [N_x, 0] else [_v[-1 if hi_y == N_y else 0] for _v in v]
      return interp(yv if bp_idx == 1 else xv, bp[bp_idx], new_v)
    else:  # This branch is taken if both x and y are in between BPs
      # Iterates through zipped low and high x values, then interpolates with x to get a new value list we can interpolate y with
      new_v = [interp(xv, [bp[0][low_x], bp[0][hi_x]], [low_xv, hi_xv]) for low_xv, hi_xv in zip(v[low_x], v[hi_x])]
      return interp(yv, [bp[1][low_y], bp[1][hi_y]], new_v)

  return [get_interp(v1, v2) for v1, v2 in zip(x, y)] if hasattr(x, '__iter__') else get_interp(x, y)

def mean(x):
  return sum(x) / len(x)

def incremental_avg(cur_avg, new_val, new_size):
  return cur_avg + ((new_val - cur_avg) / new_size)

def find_nearest_index(x, y):
  '''
  Finds nearest index of x based on the value(s) of y.
  '''
  def get_nearest(yv):
    dist = sys.maxsize
    i = 0
    xi = 0

    for xv in x:
      d = abs(abs(xv) - abs(yv))
      # print(f'd({d}) = xv({xv}) - yv({yv})')
      if d <= dist:
        dist = d
        i = xi
      xi += 1

    return i

  idxs = [get_nearest(yv) for yv in y] if hasattr(y, '__iter__') else get_nearest(y)

  # if hasattr(y, '__iter__'):
  #   for yv in y:
  #     idxs.append(get_nearest(yv))
  # else:
  #   idxs.append(get_nearest(y))

  return idxs

def is_multi_iter(x):
  multi_iter = False

  if hasattr(x, '__iter__'):
    for i in x:
      if hasattr(i, '__iter__'):
        multi_iter = True
        break

  return multi_iter
