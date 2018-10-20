"""
Signals that affect whole project.
"""

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

# pylint: disable=unused-argument
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    When a user is created, generate a token for they use the API.
    """

    if created:
        Token.objects.create(user=instance)
