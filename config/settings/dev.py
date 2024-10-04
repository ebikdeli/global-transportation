from .base import *

DEBUG = True

# SECRET_KEY = 'django-insecure-7s4l(vt1vmpatobda4utligb+b)8cxncva4y$al+kf6(i2@b5s'

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Security srttings
SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False


# These are used in django-hosts resolvers(reverse and reverse_lazy)
MAIN_PORT = 8000

MAIN_SCHEME = 'http'

PARENT_HOST = 'localhost'
