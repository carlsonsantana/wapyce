"""
Module to set custom settings for validation application.
"""

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ValidationConfig(AppConfig):
    """
    Store metadata for validation application.
    """

    name = 'wapyce.validation'
    verbose_name = _('Validation')
