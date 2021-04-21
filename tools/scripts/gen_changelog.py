#!/usr/bin/env python3
import subprocess
import requests

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

def get_commit_op_version(commit_hash):
  version = requests.get(f'https://raw.githubusercontent.com/jamcar23/openpilot/{commit_hash}/selfdrive/common/version.h').text
  version = version[version.find('"')+1:version.rfind('"')]

  # print(f'op_version: {version}')
  return version

def strip_param_line(line):
  param = line[1:].strip()
  last_char_idx = param.rfind(")")

  if last_char_idx != -1:
    param = param[0:last_char_idx + 1]

  return param

def create_indent(num_indents, single_indent='  '):
  indent = ''

  for _ in range(num_indents):
    indent += single_indent

  return indent

class Section:
  def __init__(self, title, children):
    super().__init__()

    self.title = title
    self.children = children

def create_new_params_section(cur_hash, prev_hash):
  diff = get_git_diff([prev_hash, cur_hash, '--', 'common/op_params.py'])
    # print(f'diff: {diff}')
    # break

  new_params = []

  for line in diff.splitlines():
    if not line:
      continue

    if line.startswith('+') and 'Param(' in line:
      new_params.append(strip_param_line(line))

  # print(f'new params: {new_params}')
  return Section('New OP Params', new_params)

def create_commits_section(cur_hash, prev_hash):
  commits = get_git_log([f'{prev_hash}..{cur_hash}', '--pretty=format:"%s"']).replace('"', '').splitlines()

  if ('Merge pull request #' in commits[0] and 'from jamcar23/update-' in commits[0]) or ('Merge branch \'update-' in commits[0] and 'into src' in commits[0]):
    commits = []

  commits = commits[1:][::-1]

  # print(f'commits: {commits}')
  return Section('Commits', commits)

def create_changes_from_sections(sections):
  changes = ''

  for s in sections:
    if s and s.title and len(s.children):
      changes += f'{create_indent(1)}* {s.title}:\n'
      for c in s.children:
        changes += f'{create_indent(2)}* {c}\n'

  return changes


if __name__ == '__main__':
  hashs = get_git_log(['--grep', '^Merge pull request #[0-9]\{1,\} from jamcar23', '--pretty=format:"%h"']).replace('"', '').splitlines()
  # hashs = get_git_log(['--grep="Merge pull request"', '--grep="from=jamcar23"', '--pretty=format:"%h"'])
  # print(f'hashs: {hashs}')

  changelog = ''

  for i in range(len(hashs)):
    # if i == len(hashs) - 1:
    #   break

    cur_hash = hashs[i]
    prev_hash = hashs[i + 1] if i < len(hashs) - 1 else '2fd6f3ac'

    sections = [create_new_params_section(cur_hash, prev_hash),
                create_commits_section(cur_hash, prev_hash)]

    op_version = get_commit_op_version(cur_hash)

    # break

    v_changes = f'Version {len(hashs) - i} (openpilot v{get_commit_op_version(cur_hash)})\n'
    v_changes += '========================\n'
    v_changes += create_indent(1) + f'Source commit: {cur_hash}\n'

    v_changes += create_changes_from_sections(sections)

    changelog += v_changes.strip() + '\n\n'

    # break

  with open('CHANGELOG.md', 'w') as f:
    f.write(changelog.strip() + '\n')

