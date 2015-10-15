"""
WSGI config for campus02 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "campus02.settings")

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(PROJECT_PATH)

_application = get_wsgi_application()


def application(environ, start_response):
    for key in environ:
        if key.startswith('DJANGO_'):
            os.environ[key] = environ[key]
    return _application(environ, start_response)
