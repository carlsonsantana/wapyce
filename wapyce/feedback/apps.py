"""
Module to set custom settings for feedback application.
"""

from django.apps import AppConfig
from django.utils.translation import gettext as _

class FeedbackConfig(AppConfig):
    """
    Store metadata for feedback application.
    """

    name = 'feedback'
    verbose_name = _('Feedback')
