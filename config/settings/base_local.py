"""
Django settings for wapyce project in development environment.
"""

# pylint: disable=wildcard-import, unused-wildcard-import
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = 'qe+umxbr6$u%8k@ftu=ga-js=n)b2_&=h2qav=#f5r$48d(wtu'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAPYCE_BASE_URL = 'http://localhost:8000/'
