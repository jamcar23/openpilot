#!/usr/bin/env python3
import subprocess
import requests
import re

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

class ChangeLogEntry:
  def __init__(self):
    super().__init__()

    self.fp_version = ''
    self.op_version = ''
    self.commit_hash = ''

def get_last_entry_from_log():
  lines = ''
  log_entry_pattern = re.compile(r'Version (\d+.\d+.\d) \(openpilot v([\d.]+)\)\n========================\n\s*Source commit: ([\w\d]+)')

  with open('CHANGELOG.md', 'r') as f:
    i = 0
    while i < 15:
      line = f.readline()
      if not line:
        break

      match = log_entry_pattern.search(lines)
      # print(match)
      if match:
        # print('match')
        entry = ChangeLogEntry()
        entry.fp_version = match.group(1)
        entry.op_version = match.group(2)
        entry.commit_hash = match.group(3)

        return entry

      i += 1
      lines += line

  return None

class SemVerSections:
  MAJOR = 0
  MINOR = 1
  PATCH = 2

def increment_semantic_version(version, section = SemVerSections.MAJOR):
  if not version:
    return None

  sections = version.split('.')
  # print(f'sections: {sections}')

  if section == SemVerSections.PATCH:
    sections[SemVerSections.PATCH] = str(int(sections[SemVerSections.PATCH]) + 1)
  elif section == SemVerSections.MINOR:
    sections[SemVerSections.PATCH] = '0'
    sections[SemVerSections.MINOR] = str(int(sections[SemVerSections.MINOR]) + 1)
  elif section == SemVerSections.MAJOR:
    sections[SemVerSections.PATCH] = '0'
    sections[SemVerSections.MINOR] = '0'
    sections[SemVerSections.MAJOR] = str(int(sections[SemVerSections.MAJOR]) + 1)

  return '.'.join(sections)


def main():
  hashs = get_git_log(['--grep', r'^Merge pull request #[0-9]\{1,\} from jamcar23', '--pretty=format:"%h"']).replace('"', '').splitlines()
  # hashs = get_git_log(['--grep="Merge pull request"', '--grep="from=jamcar23"', '--pretty=format:"%h"'])
  # print(f'hashs: {hashs}')

  last_written_entry = get_last_entry_from_log()
  last_entry = ChangeLogEntry()

  if last_written_entry:
    last_entry.fp_version = last_written_entry.fp_version
    last_entry.op_version = last_written_entry.op_version
    last_entry.commit_hash = last_written_entry.commit_hash
  else:
    last_entry.fp_version = '0.1.0'

  # print(last_entry.fp_version)
  changelog = ''

  for i in range(len(hashs)):
    # if i == len(hashs) - 1:
    #   break

    cur_hash = hashs[i]
    prev_hash = hashs[i + 1] if i < len(hashs) - 1 else '2fd6f3ac'

    if last_written_entry and last_written_entry.commit_hash == cur_hash:
      break

    sections = [create_new_params_section(cur_hash, prev_hash),
                create_commits_section(cur_hash, prev_hash)]

    op_version = get_commit_op_version(cur_hash)
    fp_version = increment_semantic_version(last_entry.fp_version, SemVerSections.MAJOR if op_version != last_entry.op_version else SemVerSections.MINOR)
    # print(fp_version)

    # break

    v_changes = f'Version {fp_version} (openpilot v{op_version})\n'
    v_changes += '========================\n'
    v_changes += create_indent(1) + f'Source commit: {cur_hash}\n'

    v_changes += create_changes_from_sections(sections)

    changelog += v_changes.strip() + '\n\n'

    last_entry.fp_version = fp_version
    last_entry.op_version = op_version
    last_entry.commit_hash = cur_hash

  log_lines = []
  with open('CHANGELOG.md', 'r') as f:
    log_lines = f.readlines()

  with open('CHANGELOG.md', 'w') as f:
    f.write(changelog.strip() + '\n')
    f.writelines(log_lines)

if __name__ == '__main__':
  main()