"""
Module to set custom settings for core application.
"""

from django.apps import AppConfig
from django.utils.translation import gettext as _

class CoreConfig(AppConfig):
    """
    Store metadata for core application.
    """

    name = 'core'
    verbose_name = _('Core')
