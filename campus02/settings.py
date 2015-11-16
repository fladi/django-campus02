"""
Django settings for campus02 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from IPy import IP

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DJANGO_DEBUG' in os.environ

TEMPLATE_DEBUG = DEBUG

DEBUG_TOOLBAR_PATCH_SETTINGS = False

ALLOWED_HOSTS = ['campus02.fladi.at']


class IPList(list):

    def __init__(self, ips):
        for ip in ips:
            self.append(IP(ip))

    def __contains__(self, ip):
        try:
            for net in self:
                if ip in net:
                    return True
        except:
            pass
        return False

if 'DJANGO_INTERNAL_IPS' in os.environ:
    INTERNAL_IPS = IPList(os.environ.get('DJANGO_INTERNAL_IPS').split(','))

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'django_extensions',
    'crispy_forms',
    'campus02.base',
    'campus02.web',
    'django.contrib.admin',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)

ROOT_URLCONF = 'campus02.urls'

WSGI_APPLICATION = 'campus02.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': os.environ.get(
            'DJANGO_DATABASES_DEFAULT_ENGINE',
            'django.db.backends.sqlite3'
        ),
        'NAME': os.environ.get(
            'DJANGO_DATABASES_DEFAULT_NAME',
            os.path.join(BASE_DIR, 'db.sqlite3')
        ),
        'USER': os.environ.get(
            'DJANGO_DATABASES_DEFAULT_USER',
            ''
        ),
        'PASSWORD': os.environ.get(
            'DJANGO_DATABASES_DEFAULT_PASSWORD',
            ''
        ),
        'HOST': os.environ.get(
            'DJANGO_DATABASES_DEFAULT_HOST',
            ''
        ),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
        'KEY_PREFIX': __package__
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = "/var/www/vhosts/campus02.fladi.at/static/"

STATICFILES_DIRS = (
    '/usr/share/javascript/',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'
