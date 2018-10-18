"""
Module to set custom settings for notifier application.
"""

from django.apps import AppConfig
from django.utils.translation import gettext as _

class NotifierConfig(AppConfig):
    """
    Store metadata for notifier application.
    """

    name = 'notifier'
    verbose_name = _('Notifier')
