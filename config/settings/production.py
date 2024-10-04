from .base import *

DEBUG = False

# SECRET_KEY = 'django-insecure-7s4l(vt1vmpatobda4utligb+b)8cxncva4y$al+kf6(i2@b5s'   # WILL CHANGE

# https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']   # WILL CHANGE
# In production if server returns error '400 BAD REQUEST' it means 'ALLOWED_HOSTS' is not
# set correctly

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Security srttings (These are should be True in production)
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False


# These are used in django-hosts resolvers(reverse and reverse_lazy)
MAIN_PORT = 443 if SECURE_SSL_REDIRECT else 80

MAIN_SCHEME = 'https' if SECURE_SSL_REDIRECT else 'http'

PARENT_HOST = 'rapadana.ir'

try:
    from .local import *
except ImportError:
    pass
