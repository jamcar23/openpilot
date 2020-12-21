#!/usr/bin/env python3
import sys

from tools.lib.route import Route
from tools.lib.logreader import LogReader

def main(args):
  r = Route(args[0])
  lr = LogReader(r.log_paths()[int(args[1])])


  with open(f"{args[0]}--{args[1]}.txt", "w") as f:
    f.write('\n'.join([str(msg) for msg in lr]))


if __name__ == "__main__":
    main(sys.argv[1:])
