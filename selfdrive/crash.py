"""Install exception handler for process crash."""
import os
import sys
import threading
import traceback


from selfdrive.swaglog import cloudlog
from selfdrive.hardware import PC
from datetime import datetime

if os.getenv("NOLOG") or os.getenv("NOCRASH") or PC:
  def capture_exception(*args, **kwargs):
    pass

  def bind_user(**kwargs):
    pass

  def bind_extra(**kwargs):
    pass

  def install():
    pass
else:
  from selfdrive.sentryd.sentryd import create_client

  CRASHES_DIR = '/data/community/crashes'
  if not os.path.exists(CRASHES_DIR):
    os.makedirs(CRASHES_DIR)

  client = create_client()
  def save_exception(exc_text):
    log_file = '{}/{}'.format(CRASHES_DIR, datetime.now().strftime('%m-%d-%Y--%I:%M.%S-%p.log'))
    with open(log_file, 'w') as f:
      f.write(exc_text)
    print('Logged current crash to {}'.format(log_file))

  def capture_exception(*args, **kwargs):
    save_exception(traceback.format_exc())
    client.captureException(*args, **kwargs)
    cloudlog.error("crash", exc_info=kwargs.get('exc_info', sys.exc_info()))

  def bind_user(**kwargs):
    client.user_context(kwargs)

  def bind_extra(**kwargs):
    client.extra_context(kwargs)

  def install():
    """
    Workaround for `sys.excepthook` thread bug from:
    http://bugs.python.org/issue1230540
    Call once from the main thread before creating any threads.
    Source: https://stackoverflow.com/a/31622038
    """
    # installs a sys.excepthook
    __excepthook__ = sys.excepthook

    def handle_exception(*exc_info):
      if exc_info[0] not in (KeyboardInterrupt, SystemExit):
        capture_exception()
      __excepthook__(*exc_info)
    sys.excepthook = handle_exception

    init_original = threading.Thread.__init__

    def init(self, *args, **kwargs):
      init_original(self, *args, **kwargs)
      run_original = self.run

      def run_with_except_hook(*args2, **kwargs2):
        try:
          run_original(*args2, **kwargs2)
        except Exception:
          sys.excepthook(*sys.exc_info())

      self.run = run_with_except_hook

    threading.Thread.__init__ = init
