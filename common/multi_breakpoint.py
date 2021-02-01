def is_multi_iter(x):
  multi_iter = False

  if hasattr(x, '__iter__'):
    for i in x:
      if hasattr(i, '__iter__'):
        multi_iter = True
        break

  return multi_iter

def correct_multi_breakpoint_points(bp, idx=-1):
  if not is_multi_iter(bp[idx]):
    bp[idx] = [bp[idx], bp[idx]]

    if len(bp) <= 1:
      bp.insert(0, bp[idx][0])
