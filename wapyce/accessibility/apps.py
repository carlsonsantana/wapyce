"""
Module to set custom settings for accessibility application.
"""

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class AccessibilityConfig(AppConfig):
    """
    Store metadata for accessibility application.
    """

    name = 'wapyce.accessibility'
    verbose_name = _('Accessibility')
