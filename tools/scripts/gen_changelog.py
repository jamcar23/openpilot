#!/usr/bin/env python3
import subprocess
import requests
import re
import sys

from typing import List, Optional

# TODO add this back, it's causing problems with windows, git, and docker
#from selfdrive.version import run_cmd_default

DOCUMENTED_PARAM_KEYS = []

def run_cmd(cmd: List[str]) -> str:
  # print(f'cmd: {cmd}')
  with subprocess.Popen(cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:
    output, err = p.communicate()

    if p.returncode != 0:
      raise subprocess.CalledProcessError(p.returncode, cmd, output, err)

    return output


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
  req = requests.get(f'https://raw.githubusercontent.com/jamcar23/openpilot/{commit_hash}/selfdrive/common/version.h')
  version = req.text

  if not req.ok or not version:
    version = run_cmd_default(['git', 'show', f'{commit_hash}:selfdrive/common/version.h'])

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

  old_params = []
  new_params = []

  for line in diff.splitlines():
    if not line:
      continue

    if line.startswith('-') and 'Param(' in line:
      old_params.append(strip_param_line(line))
    if line.startswith('+') and 'Param(' in line:
      param_line = strip_param_line(line)
      param_key = param_line[0:param_line.find(':') + 1]

      if param_key in DOCUMENTED_PARAM_KEYS:
        continue

      found_old_param = False

      for old_param in old_params:
        if old_param.startswith(param_key):
          found_old_param = True
          break

      if not found_old_param:
        new_params.append(param_line)
        DOCUMENTED_PARAM_KEYS.append(param_key)

  # print(f'new params: {new_params}')
  return Section('New OP Params', new_params)

def create_commits_section(cur_hash, prev_hash):
  commits = get_git_log([f'{prev_hash}..{cur_hash}', '--pretty=format:"%s"']).replace('"', '').splitlines()

  if ('Merge pull request #' in commits[0] and 'from jamcar23/update-' in commits[0]) or ('Merge branch \'update-' in commits[0] and 'into src' in commits[0]) or 'bump version' in commits[0]:
    commits = []

  commits = commits[::-1]

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
  log_entry_pattern = re.compile(r'Version (\d+.\d+.\d+) \(openpilot v([\d.]+)\)\n========================\n\s*Source commit: ([\w\d]+)')

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

def get_next_semantic_version_number(last_entry, op_version):
  if last_entry.fp_version and op_version != last_entry.op_version:
    semver_change = SemVerSections.MAJOR
  else:
    semver_change = SemVerSections.MINOR

  return increment_semantic_version(last_entry.fp_version, semver_change) if last_entry.fp_version else '1.0.0'

def export_next_semver_number():
  last_entry = get_last_entry_from_log()
  last_commit = get_git_log(['-1', '--pretty=format:"%h"']).replace('"', '').strip()
  op_version = get_commit_op_version(last_commit)

  print(get_next_semantic_version_number(last_entry, op_version))

class PullRequest:
  def __init__(self, commit_hash, base_hash, head_hash):
    super().__init__()

    self.hash = commit_hash
    self.base_hash = base_hash
    self.head_hash = head_hash

def get_op_version_changelog():
  op_version_pattern = re.compile(r'Version ([\d.]+) \(\d\d\d\d-\d\d-\d\d\)')
  op_log_seperator_pattern = re.compile(r'[=]+')
  versions = {}

  with open('RELEASES.md', 'r') as f:
    lines = f.readlines()

  # print(f'lines: {lines}')
  i = 0
  while i < len(lines):
    line = lines[i].strip()
    match = op_version_pattern.search(line)
    changes = []

    # if match:
    #   print('op release version match')
    #   print(f'line + 1: {lines[i + 1]}')

    if match and op_log_seperator_pattern.search(lines[i + 1].strip()):
      # print('op release version match')
      o = 2
      ll = lines[i + o].strip()
      # print(f'll: {ll}')

      while ll.startswith('*'):
        changes.append(ll[1:])
        o += 1
        ll = lines[i + o].strip()

    if len(changes):
      versions[match.group(1)] = changes
      i += len(changes)

    i += 1

  # print(f'op releases: {versions}')
  return versions

def main():
  commit_logs = get_git_log(['--grep', r'^Merge pull request #[0-9]\{1,\} from jamcar23', '--pretty=short'])
  # hashs = get_git_log(['--grep="Merge pull request"', '--grep="from=jamcar23"', '--pretty=format:"%h"'])
  # print(f'hashs: {hashs}')

  pr_hash_pattern = re.compile(r'commit ([\w\d]+)\nMerge: ([\w\d][\w\d][\w\d][\w\d][\w\d][\w\d][\w\d][\w\d]) ([\w\d][\w\d][\w\d][\w\d][\w\d][\w\d][\w\d][\w\d])')
  prs = pr_hash_pattern.findall(commit_logs)

  hashs = []

  for pr in prs:
    hashs.append(PullRequest(pr[0][0:8], pr[1], pr[2]))

  hashs = hashs[::-1]
  # print(hashs[0].hash)
  # print(f'hashs: {hashs}')
  # return
  last_written_entry = get_last_entry_from_log()
  last_entry = ChangeLogEntry()

  if last_written_entry:
    last_entry.fp_version = last_written_entry.fp_version
    last_entry.op_version = last_written_entry.op_version
    last_entry.commit_hash = last_written_entry.commit_hash

    trim_hashs = False
    hash_idx = 0

    for h in hashs:
      if h.hash == last_entry.commit_hash:
        trim_hashs = True
        break
      hash_idx += 1

    if trim_hashs:
      hashs = hashs[hash_idx + 1:]

  # print(last_entry.fp_version)
  op_releases = get_op_version_changelog()
  changelog = ''

  for i in range(len(hashs)):
    # if i == len(hashs) - 1:
    #   break

    cur_hash = hashs[i]
    prev_hash = hashs[i - 1].hash if i >= 1 else last_written_entry.commit_hash if last_written_entry else '2fd6f3ac'

    if last_written_entry and last_written_entry.commit_hash == cur_hash:
      pass
      # break

    sections = [create_new_params_section(cur_hash.hash, prev_hash),
                create_commits_section(cur_hash.head_hash, cur_hash.base_hash)]

    op_version = get_commit_op_version(cur_hash.hash)

    if last_entry.fp_version and op_version != last_entry.op_version:
      sections[1] = Section('Openpilot Changes', op_releases[op_version])

    fp_version = get_next_semantic_version_number(last_entry, op_version)
    # print(fp_version)

    # break

    v_changes = f'Version {fp_version} (openpilot v{op_version})\n'
    v_changes += '========================\n'
    v_changes += create_indent(1) + f'Source commit: {cur_hash.hash}\n'

    v_changes += create_changes_from_sections(sections)

    changelog = v_changes.strip() + '\n\n' + changelog

    last_entry.fp_version = fp_version
    last_entry.op_version = op_version
    last_entry.commit_hash = cur_hash.hash

  if changelog:
    log_lines = []
    with open('CHANGELOG.md', 'r') as f:
      log_lines = f.readlines()

    with open('CHANGELOG.md', 'w') as f:
      f.write(changelog.strip() + '\n\n')
      f.writelines(log_lines)

if __name__ == '__main__':
  args = sys.argv[1:]

  if '--export' in args:
    export_next_semver_number()
  else:
    main()
