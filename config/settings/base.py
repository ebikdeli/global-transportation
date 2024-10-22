"""
If you include rich text editors like 'CKEditor' or 'django_quill' into project, make sure to enter:
'py manage.py collectstatic'.

We can use 'Django Two-Factor Authentication' module for better security. For more
information use below document:
https://django-two-factor-auth.readthedocs.io/en/1.14.0/
NOTE: If we don't want to use django-two-factor-authentication module, we MUST COMMENT ALL
settings, configs, apps, middleware, urls and etc of the module.

To load static and media files from AWS (or any other CDN provider) we better used following modules:
'boto3' and 'django-storages'.
"""
from django.urls import reverse_lazy
import os
from dotenv import load_dotenv, dotenv_values
# from pathlib import Path


load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = dotenv_values()['SECRET_KEY']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    "debug_toolbar",
    'django_filters',
    'taggit',
    'django_countries',
    'social_django',
    'corsheaders',
    # 'django_hosts',
    'ckeditor',
    'ckeditor_uploader',
    'axes',
    # https://github.com/jazzband/django-axes/issues/915	# Issue with django=4.1 and django-axes
    'silk',
    # 'admin_honeypot',
    'sorl.thumbnail',
    'constance',
    # "django_minify_html",

    # We need these modules to activate 'django two-factor-authentication':
    # 'django_otp',
    # 'django_otp.plugins.otp_static',
    # 'django_otp.plugins.otp_totp',
    # 'django_otp.plugins.otp_email',  # <- if you want email capability.
    # 'two_factor',
    # 'two_factor.plugins.phonenumber',  # <- if you want phone number capability.
    # 'two_factor.plugins.email',  # <- if you want email capability.
    # 'two_factor.plugins.yubikey',  # <- for yubikey capability.

    # "django_browser_reload",    # Enable 'django-browser-reload' module
    'watchman',     # Enable 'django-watchman'
    # NOTE: If 'watchman' causes this error: "ImportError: cannot import name '__version__'...", we
    # need to just got to .../env/watchamn/__init__.py directory and add this line:
    # __version__= '<installed_watchman_version>' for eg: __version__ = '1.3.0' 

    # 'accounts.apps.AccountsConfig',	# <==> For signals this is better than simple 'accounts'
    # ABOVE LINE NOT NEEDED AFTER DJANGO==3.2 and just 'accounts' is enought.

    # If 'account' or any other application is in another folder relative to absolute path to project base directory we
    # (eg: this folder named 'apps' relative to base dir: './apps/') we just need to do this:
    # !!! don't name your user management app 'account' or 'accounts' because django allauth package uses these name and urls
    # 'apps.accounts',

    # To be able to use database for 'constance'
    # 'constance.backends.database',
    'main',
    'users',
    'shipping',
    'payment',
]


MIDDLEWARE = [
    # 'django_hosts.middleware.HostsRequestMiddleware',       # To activate 'django-hosts'

    "debug_toolbar.middleware.DebugToolbarMiddleware",    # To enable 'django-debug-tool'
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',        # for per site cache
    'corsheaders.middleware.CorsMiddleware',                # To activate 'cors-headers'
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',     # for per site cache
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    
    'silk.middleware.SilkyMiddleware',				   # To enable django-silk

    # 'django_otp.middleware.OTPMiddleware',                  # To activate 'django-two-factor-authentication'
    
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # "django_minify_html.middleware.MinifyHtmlMiddleware",   # To enable django_minify_html to load pages much faster

    # 'django_browser_reload.middleware.BrowserReloadMiddleware',     # 'django-browser-reload' module

    # 'django_hosts.middleware.HostsResponseMiddleware',      # To activate 'django-hosts'
    'axes.middleware.AxesMiddleware',                       # To acitave 'django-axes'
    # 'django_session_timeout.middleware.SessionTimeoutMiddleware',    # To activate 'django_session_timeout'
]


ROOT_URLCONF = 'config.urls'

# For django_hosts
ROOT_HOSTCONF = '<project_name>.hosts'

DEFAULT_HOST = 'www'
# We moved following settings to 'dev.py' and 'production.py'
# This is needed to use django-hosts 'reverse' function but should change in production!
# PARENT_HOST = 'localhost'
"""
# This is an example of how we can use django-hosts reverse function in production:
# With example of a subdomain named 'www' with address of 'www', app named 'blog' and a view named 'blog_detail' and
# a url with variable .../<slug:slug>/... (And note that below code is in 'rapadana' project, blog.view.CreateBlogView
url = reverse(viewname='blog:blog_detail', kwargs={'slug': self.object.slug}, host_args=('www',), host='www', scheme='http', port='8000')
"""
# PARENT_HOST = 'localhost' if settings.DEBUG else 'example.com'

# if settings.DEBUG:
#     MAIN_PORT = 8000
# else:
#     MAIN_PORT = 443 if settings.SECURE_SSL_REDIRECT else 80

# MAIN_PORT = 8000 if settings.DEBUG else 443 if settings.SECURE_SSL_REDIRECT else 80

# MAIN_SCHEME = 'http' if settings.DEBUG else 'https' if settings.SECURE_SSL_REDIRECT else 'http'


# Templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,  os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                # 'cart.context_processor.cart_context'
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'timeout': 20,
                    }
    }
}


# Using django memcache for caching
"""
CACHES = {
    'default': {
        'BACKEND': 'djpymemcache.backend.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 600                                        # cache never expires
    }
}
"""

# for cache per site:

# CACHE_MIDDLEWARE_ALIAS = 'apadana_cache'

# CACHE_MIDDLEWARE_SECONDS = 900

# CACHE_MIDDLEWARE_KEY_PREFIX = 'mem'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTH_USER_MODEL = 'users.User'
# AUTH_USER_MODEL = 'accounts.User'


# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = True

THOUSAND_SEPARATOR = ','

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
# To deploy on Host (Sub folders do not accepted by host!):
# STATIC_ROOT = '/home/<serivce_name>/public_html/static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR),
    os.path.join(BASE_DIR, 'statics'),
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# To deploy on Host:
# MEDIA_ROOT = '/home/<serivce_name>/public_html/media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Login and Logout urls (django 'two-factor-authentication' overrides these settings)
# https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#reversing-admin-urls

# LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = reverse_lazy('admin:login')

# LOGIN_URL = '/login/'
LOGIN_URL = 'admin:login'

# If for example we have
# LOGOUT_REDIRECT_URL = 'blog:blog_list'
# LOGOUT_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'index'

# We can also use 'reverse_lazy' to handle login and logout urls like above examples but we can
# not to use 'reverse_lazy' (but it's recommended for good practice).


TAGGIT_CASE_INSENSITIVE = True


# Django social authentication settings:

# SOCIAL_AUTH_POSTGRES_JSONFIELD = True     <==> This is soon to be decapitated
# SOCIAL_AUTH_JSONFIELD_ENABLED = True

"""
AUTHENTICATION_BACKENDS = (
    # google oauth2 backend
    'social_core.backends.google.GoogleOAuth2',

    # normal django auth backend
    'django.contrib.auth.backends.ModelBackend',
)
"""

# ID_KEY and SECRET for google
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '696613813066-qi854fm95mv3h7meen44rbqgcel48mbu.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'KM1oanQONJYFvgtT9BVGu9gy'

# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [...]

# SOCIAL_AUTH_URL_NAMESPACE = 'social'    # It's optional, to make a default namespace for our social auth backend


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ]
}


# Cors headers settings (NOTE: Without 'cors', process on diffrent domains and ports could not speak to each other! 'same-origin' only enabled when two process work on same domain and port)
# In ajax request using 'fetch' or any front techs like 'reqct', 'angular' or even an script with 'requests' library, we must enable 'CORS' for the server.
# NOTE: Many techs habe problems with 'CORS_ALLOW_ALL_ORIGINS = True' like 'fetch' in JS. So use 'CORS_ALLOWED_ORIGIN' to escape that problem!
# CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",
    'http://127.0.0.1:5500',
    'https://127.0.0.1:5500',
]
# * If we don't set 'CORS_ALLOW_CREDENTIALS = True', We will get this error on client side:
# Access to fetch at 'http://127.0.0.1:8000/add_product_cart' from origin 'http://127.0.0.1:5500' has been blocked by CORS policy: The value of the 'Access-Control-Allow-Credentials' header in the response is '' which must be 'true' when the request's credentials mode is 'include'.
# NOTE: Remember that without this field, any cookie sent by client, does not checked by server!
# CORS_ALLOW_CREDENTIALS = True

# * To be able to let 'X-CSRFToken' header checked by server (this header sent by any client) we must 
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
    'http://*:*'
]



# CKEditor settings
# each one of three below is acceptable
# CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
# CKEDITOR_BASEPATH = f"{STATIC_URL}ckeditor/ckeditor/"
CKEDITOR_BASEPATH = (os.path.join(STATIC_URL, 'ckeditor', 'ckeditor', '')).replace("\\", "/")		# Works on windows machine
CKEDITOR_UPLOAD_PATH = "uploads/"

# CKEditor optional settings
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'toolbar': 'basic',
        'height': 300,
        'width': 300,
    },
}


# django-axes optional config:
# https://django-axes.readthedocs.io/en/latest/4_configuration.html

AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesBackend',
    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

# AXES_FAILURE_LIMIT = 5
# AXES_ONLY_USER_FAILURES = True


# django-constance settings
CONSTANCE_CONFIG = {
    'discount': (5, 'Global discount percent'),
}

CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True

# By default django uses 'redis' to store 'constance' variables. to use database we should follow this document:
# https://django-constance.readthedocs.io/en/latest/backends.html#database
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'


# Django two factor authentication
# LOGIN_URL = 'two_factor:login'

# this one is optional
# LOGIN_REDIRECT_URL = 'two_factor:profile'


# django-debug-toolbar settings

# INTERNAL_IPS = [
#     # ...
#     "127.0.0.1",
#     # ...
# ]


# django-session-timeout settings

# SESSION_EXPIRE_SECONDS = 3600  # 1 hour
# SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
# SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60 # group by minute
# SESSION_TIMEOUT_REDIRECT = 'your_redirect_url_here/'


# ! To authenticate email server, we either have to use ('EMAIL_PORT=587', 'EMAIL_USE_TLS=True') or ('EMAIL_PORT=465', 'EMAIL_USE_SSL=True'). We cannot use both
# ? Both of SSL and TSL works, but it looks ('EMAIL_PORT=587', 'EMAIL_USE_TLS=True') is faster
# EMAIL_HOST = 'mail.dornika.shop'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# # EMAIL_PORT = 465
# # EMAIL_USE_SSL = True
# EMAIL_HOST_USER = 'dornika@dornika.shop'
# EMAIL_HOST_PASSWORD = 'dornikashop'
