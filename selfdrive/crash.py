"""Install exception handler for process crash."""
import os
import sys
import traceback
from datetime import datetime
from selfdrive.swaglog import cloudlog
from selfdrive.version import version

import sentry_sdk
from sentry_sdk.integrations.threading import ThreadingIntegration

CRASHES_DIR = '/data/community/crashes'

def save_exception(exc_text):
  if not os.path.exists(CRASHES_DIR):
    os.makedirs(CRASHES_DIR)

  log_file = '{}/{}'.format(CRASHES_DIR, datetime.now().strftime('%m-%d-%Y--%I:%M.%S-%p.log'))
  with open(log_file, 'w') as f:
    f.write(exc_text)
  print('Logged current crash to {}'.format(log_file))

def capture_exception(*args, **kwargs) -> None:
  cloudlog.error("crash", exc_info=kwargs.get('exc_info', 1))

  try:
    save_exception(traceback.format_exc())
    sentry_sdk.capture_exception(*args, **kwargs)
    sentry_sdk.flush()  # https://github.com/getsentry/sentry-python/issues/291
  except Exception:
    cloudlog.exception("sentry exception")

def bind_user(**kwargs) -> None:
  sentry_sdk.set_user(kwargs)

def bind_extra(**kwargs) -> None:
  for k, v in kwargs.items():
    sentry_sdk.set_tag(k, v)

def init() -> None:
  sentry_sdk.init("https://ee3dca66da104ef388e010fcefbd06c6:df79d17e3a0743c387d4cbf05932abde@o484202.ingest.sentry.io/5537090",
                  default_integrations=False, integrations=[ThreadingIntegration(propagate_hub=True)],
                  release=version)
