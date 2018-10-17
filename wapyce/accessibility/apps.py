"""
Module to set custom settings for accessibility application.
"""

from django.apps import AppConfig
from django.utils.translation import gettext as _

class AccessibilityConfig(AppConfig):
    """
    Store metadata for accessibility application.
    """

    name = 'accessibility'
    verbose_name = _('Accessibility')
