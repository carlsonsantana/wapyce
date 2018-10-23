"""
Models of accessibility app.
"""

from django.db import models
from django.utils.translation import gettext as _

from wapyce.core.models import CoreModel
from wapyce.validation.models import Page

# Create your models here.

class IssueCode(models.Model):
    """
    The IssueCode class is a model that represents a code of a issue of page.
    """

    code = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Issue code')
    )

    class Meta:
        """
        Metadata class of issue code model.
        """

        verbose_name = _('Issue code')

    def __str__(self):
        return self.code

class IssuePage(CoreModel):
    """
    The IssuePage class is a model that represents a issue of page.
    """

    ERROR = 1
    WARNING = 2
    NOTICE = 3
    TYPE_CHOICES = (
        (ERROR, _('Error')),
        (WARNING, _('Warning')),
        (NOTICE, _('Notice')),
    )

    page = models.ForeignKey(
        Page,
        on_delete=models.PROTECT,
        verbose_name=_('Page URL')
    )
    code = models.ForeignKey(
        IssueCode,
        on_delete=models.PROTECT,
        verbose_name=_('Issue code')
    )
    context = models.CharField(max_length=255, verbose_name=_('Context'))
    message = models.CharField(max_length=255, verbose_name=_('Message'))
    selector = models.CharField(max_length=200, verbose_name=_('Selector'))
    issue_type = models.IntegerField(
        choices=TYPE_CHOICES,
        verbose_name=_('Type')
    )

    class Meta:
        """
        Metadata class of issue model.
        """

        verbose_name = _('Issue of page')
