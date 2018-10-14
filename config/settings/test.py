"""
Django settings for wapyce project in test environment.
"""

# pylint: disable=wildcard-import, unused-wildcard-import, unused-import
from .base import *
from .local import DEBUG
from .local import ALLOWED_HOSTS
from .local import SECRET_KEY
from .local import EMAIL_BACKEND

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_variable('DATABASE_TEST_NAME'),
        'USER': get_env_variable('DATABASE_TEST_USER'),
        'PASSWORD': get_env_variable('DATABASE_TEST_PASSWORD'),
        'HOST': get_env_variable('DATABASE_TEST_HOST'),
        'PORT': get_env_variable('DATABASE_TEST_PORT')
    }
}
