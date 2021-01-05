import json
import os
import sys

from common.file_helpers import mkdirs_exists_ok
from selfdrive.hardware import PC


class MissingAuthConfigError(Exception):
  pass


if PC:
  CONFIG_DIR = os.path.expanduser('~/.comma')
else:
  CONFIG_DIR = "/tmp/.comma"

mkdirs_exists_ok(CONFIG_DIR)


def get_token():
  try:
    with open(os.path.join(CONFIG_DIR, 'auth.json')) as f:
      auth = json.load(f)
      return auth['access_token']
  except Exception as e:
    raise MissingAuthConfigError('Authenticate with tools/lib/auth.py') from e


def set_token(token):
  with open(os.path.join(CONFIG_DIR, 'auth.json'), 'w') as f:
    json.dump({'access_token': token}, f)


def clear_token():
  os.unlink(os.path.join(CONFIG_DIR, 'auth.json'))


if __name__ == "__main__":
  l = len(sys.argv)

  if l == 2:
    set_token(sys.argv[1])
  elif l == 1:
    clear_token()
  else:
    print('Unknown number of args.')
