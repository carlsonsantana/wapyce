"""
Models classes inherited for models of other apps.
"""

import uuid as uuid_lib

from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class CoreModel(models.Model):
    """
    The CoreModel class is a abstract model that has common fields and methods.
    """

    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False,
        verbose_name=_('Universally unique identifier')
    )

    class Meta:
        """
        Metadata class of core model.
        """

        abstract = True
