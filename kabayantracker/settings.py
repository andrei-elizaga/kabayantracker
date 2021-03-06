import os

from os.path import dirname, abspath, join, pardir

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DIRNAME = os.path.dirname(os.path.normpath(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qvrcxoye9$#vbx0*k-_&gu)^(g5)kq4l#ycl-w&61onj_6hz$)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',

    'main',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kabayantracker.urls'

WSGI_APPLICATION = 'kabayantracker.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, '../templates/'),
)


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'kabayantracker',        # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, '../static/')
STATIC_URL = '/static/'

LOG_DIR = os.path.join(PROJECT_ROOT, '../../log/')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "%(asctime)s %(levelname)s %(filename)s %(lineno)s : %(message)s",
            'datefmt': "%y/%m/%d %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s : %(message)s',
            'datefmt': '%y/%m/%d, %H:%M:%S',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {'level': 'DEBUG',
                 'class': 'django.utils.log.NullHandler'},
        'console': {'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'simple'},
        'app': {'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_DIR, 'kabayantracker.log'),
                'formatter': 'standard',
                'maxBytes': 1024 * 1024 * 50}},
    'loggers': {'django': {'handlers': ['null'],
                           'propagate': True,
                           'level': 'INFO'}}
}

try:
    from local_settings import *
except ImportError:
    pass
