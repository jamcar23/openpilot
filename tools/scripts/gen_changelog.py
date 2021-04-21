#!/usr/bin/env python3
import subprocess
from typing import List, Optional

# TODO add this back, it's causing problems with windows, git, and docker
#from selfdrive.version import run_cmd_default

def run_cmd(cmd: List[str]) -> str:
  # print(f'cmd: {cmd}')
  return subprocess.check_output(cmd, encoding='utf8', shell=True).strip()


def run_cmd_default(cmd: List[str], default: Optional[str] = None) -> Optional[str]:
  try:
    return run_cmd(cmd)
  except subprocess.CalledProcessError:
    return default

def get_git_log(cmd: List[str], default: Optional[str] = None) -> Optional[str]:
  # print(f'cmd: {["git", "log" ] + cmd}')
  return run_cmd_default(['git', 'log', ] + cmd, default)

def get_git_diff(cmd: List[str], default: Optional[str] = None) -> Optional[str]:
  return run_cmd_default(['git', 'diff', ] + cmd, default)


if __name__ == '__main__':
  hashs = get_git_log(['--grep', '^Merge pull request #[0-9]\{1,\} from jamcar23', '--pretty=format:"%h"']).replace('"', '').splitlines()
  # hashs = get_git_log(['--grep="Merge pull request"', '--grep="from=jamcar23"', '--pretty=format:"%h"'])
  print(f'hashs: {hashs}')

  changelog = ''

  for i in range(len(hashs)):
    if i == len(hashs) - 1:
      break

    diff = get_git_diff([hashs[i + 1], hashs[i], '--', 'common/op_params.py'])
    print(f'diff: {diff}')
    break

  #   v_changes = f'Version {len(hashs) - i}\n'
  #   v_changes += '========================\n'
  #   v_changes += diff
  #   v_changes += '\n\n'

  #   changelog += v_changes

  # with open('CHANGELOG.md', 'w') as f:
  #   f.write(changelog)

