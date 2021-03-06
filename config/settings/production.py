"""
Django settings for wapyce project in production environment.
"""

# pylint: disable=wildcard-import, unused-wildcard-import
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable('SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_variable('DATABASE_NAME'),
        'USER': get_env_variable('DATABASE_USER'),
        'PASSWORD': get_env_variable('DATABASE_PASSWORD'),
        'HOST': get_env_variable('DATABASE_HOST'),
        'PORT': get_env_variable('DATABASE_PORT')
    }
}

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

SOCIAL_AUTH_GITHUB_KEY = get_env_variable('GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = get_env_variable('GITHUB_SECRET')
GITHUB_PERSONAL_ACCESS_TOKEN = get_env_variable('GITHUB_PERSONAL_ACCESS_TOKEN')
WAPYCE_BASE_URL = get_env_variable('WAPYCE_BASE_URL')

# Security
# https://docs.djangoproject.com/en/2.1/topics/security/

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True
