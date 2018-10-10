"""
Django settings for wapyce project in development environment.
"""

# pylint: disable=wildcard-import, unused-wildcard-import
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_local.sqlite3'),
    }
}
