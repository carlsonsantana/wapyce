"""
Models of validation app.
"""

from django.db import models
from django.utils.translation import gettext as _

from .validators import validate_github_url

# Create your models here.

# pylint: disable=too-few-public-methods
class Site(models.Model):
    """
    The Site class is a model that represents a site that will be validated.
    """

    name = models.CharField(max_length=100, verbose_name=_('Name'))
    base_url = models.URLField(unique=True, verbose_name=_('Base URL'))
    github_url = models.URLField(
        unique=True,
        verbose_name=_('Github repository'),
        validators=[validate_github_url]
    )

    class Meta:
        """
        Metadata class of site model.
        """

        verbose_name = _('Site')

    def __str__(self):
        return '{} ({})'.format(self.name, self.base_url)
