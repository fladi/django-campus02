"""
Django settings for campus02 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from IPy import IP

BASE_DIR = os.path.abspath(os.path.join(__file__, '../..'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')
TMDB_API_KEY = os.environ.get('DJANGO_TMDB_API_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DJANGO_DEBUG' in os.environ

DEBUG_TOOLBAR_PATCH_SETTINGS = False

ALLOWED_HOSTS = ['campus02.fladi.at']


class IPList(list):

    def __init__(self, addresses):
        super(IPList, self).__init__()
        for address in addresses:
            self.append(IP(address))

    def __contains__(self, address):
        try:
            for net in self:
                if address in net:
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
    'campus02.base',
    'campus02.web',
    'rest_framework',
    'guardian',
    'reversion',
    'corsheaders',
    'debug_toolbar',
    'django_extensions',
    'crispy_forms',
    'django_uwsgi',
    'django.contrib.admin',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG
        },
    },
]

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
        'BACKEND': 'django_redis.cache.RedisCache',
        #'LOCATION': 'redis://localhost:6379/1',
        'LOCATION': 'unix:///var/run/redis/redis.sock?db=1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'KEY_PREFIX': __package__
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    '/usr/share/javascript/',
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap3'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

CORS_ORIGIN_ALLOW_ALL = True

RUNSERVERPLUS_SERVER_ADDRESS_PORT = '0.0.0.0:8087'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'werkzeug': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
