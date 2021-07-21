# import os

# from raven import Client
# from raven.transport.http import HTTPTransport

# from common.op_params import opParams
# from selfdrive.version import version, dirty
# from selfdrive.version import origin, branch, commit

# _USERNAME = None

# def get_username():
#     global _USERNAME
#     if _USERNAME:
#         return _USERNAME

#     _USERNAME = opParams().get('username')

#     if _USERNAME is None or not isinstance(_USERNAME, str):
#         _USERNAME = ''

#     return _USERNAME

# def create_standard_tags():
#     return {'dirty': dirty, 'origin': origin, 'branch': branch, 'commit': commit}

# def create_client(*args, tags=None, **kwargs):
#     if not tags:
#         tags = create_standard_tags()

#     client = Client('https://ee3dca66da104ef388e010fcefbd06c6:df79d17e3a0743c387d4cbf05932abde@o484202.ingest.sentry.io/5537090',
#                   install_sys_hook=False, transport=HTTPTransport, release=version, tags=tags, *args, **kwargs)

#     username = get_username()
#     user_context = {}

#     if username:
#         user_context['username'] = username

#     user_context['dongle_id'] = os.environ.get('DONGLE_ID')

#     client.user_context(user_context)

#     return client

# def sentryd_thread():
#     pass

# if __name__ == "__main__":
#     sentryd_thread()
