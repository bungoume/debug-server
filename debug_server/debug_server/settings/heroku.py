from debug_server.settings import *  # NOQA


ALLOWED_HOSTS = ['*']

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
