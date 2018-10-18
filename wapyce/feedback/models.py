"""
Models of feedback app.
"""

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _

from wapyce.validation.models import ValidationGroup
from wapyce.validation.models import Validation

# Create your models here.

class FeedbackValidation(models.Model):
    """
    The FeedbackValidation class is a model that represents a feedback of
    validations.
    """

    validation_group = models.ForeignKey(
        ValidationGroup,
        on_delete=models.PROTECT,
        verbose_name=_('Validation group')
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name=_('User')
    )
    approved = models.BooleanField(verbose_name=_('Approved'))
    date_feedback = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Date of feedback')
    )

    class Meta:
        """
        Metadata class of validations feedback model.
        """

        verbose_name = _('Validations feedback')
        unique_together = ('validation_group', 'user')

    def clean(self):
        super(FeedbackValidation, self).clean()

        if (
            Validation.objects.filter(
                group=self.validation_group,
                user=self.user
            ).exists()
        ):
            raise ValidationError(_(
                'The user "{}", can\'t send a feedback of site because'
                + ' they validate it.'
            ))
