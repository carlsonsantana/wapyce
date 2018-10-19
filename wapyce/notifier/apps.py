"""
Module to set custom settings for notifier application.
"""

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class NotifierConfig(AppConfig):
    """
    Store metadata for notifier application.
    """

    name = 'wapyce.notifier'
    verbose_name = _('Notifier')
