"""
Models of notifier app.
"""

from django.db import models
from django.utils.translation import gettext as _

from wapyce.validation.models import Validation

# Create your models here.

class GithubIssue(models.Model):
    """
    The GithubIssue class is a model that represents a issue of GitHub.
    """

    validation_site = models.ForeignKey(
        Validation,
        on_delete=models.PROTECT,
        verbose_name=_('Validation')
    )
    number = models.IntegerField(verbose_name=_('Number of GitHub issue'))
    created_at = models.DateTimeField(verbose_name=_('Created at'))

    class Meta:
        """
        Metadata class of GitHub issue model.
        """

        verbose_name = _('GitHub issue')
