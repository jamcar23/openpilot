#!/usr/bin/env python3
from typing import List, Optional

from selfdrive.version import run_cmd_default

def get_git_log(cmd: List[str], default: Optional[str] = None) -> Optional[str]:
  return run_cmd_default(['git', 'log', ] + cmd, default)


if __name__ == '__main__':
  print(get_git_log(['--grep="Merge pull request"', '--grep="from=jamcar23"', '--pretty=format:"%h"']))
