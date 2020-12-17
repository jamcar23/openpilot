def int_rnd(x):
  return int(round(x))

def clip(x, lo, hi):
  return max(lo, min(hi, x))

def interp(x, xp, fp):
  N = len(xp)
  T = len(fp)

  def get_interp(xv):
    def calc_interp(l, h):
      return (xv - xp[l]) * (fp[h] - fp[l]) / (xp[h] - xp[l]) + fp[l]

    hi = 0
    while hi < N and xv > xp[hi]:
      hi += 1
    low = hi - 1
    return fp[-1] if hi >= T or low >= T or (hi >= N and xv >= xp[low]) or (N < T and fp[N - 1] == calc_interp(N - 2, N - 1)) else (
      fp[0] if hi == 0 else
      calc_interp(low, hi))

  return [get_interp(v) for v in x] if hasattr(x, '__iter__') else get_interp(x)

def mean(x):
  return sum(x) / len(x)

def incremental_avg(cur_avg, new_val, new_size):
  return cur_avg + ((new_val - cur_avg) / new_size)
