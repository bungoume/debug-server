from debug_server.settings import *  # NOQA


ALLOWED_HOSTS = ['*']

DEBUG = False

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY') or SECRET_KEY
TIME_ZONE = os.environ.get('TIME_ZONE') or TIME_ZONE
