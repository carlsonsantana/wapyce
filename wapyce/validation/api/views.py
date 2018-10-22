"""
Views of API validation application.
"""

from django.db.models import Q
from django.utils.translation import gettext as _

from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from wapyce.validation.models import Site
from wapyce.validation.models import Validation
from wapyce.validation.models import ValidationGroup
from .serializers import ValidationSerializer

class NewValidationAPIView(CreateAPIView):
    """
    View of API to register the start of validation of user.
    """

    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """
        Register the start of validation of user, if they not has a validation
        started.
        """

        user = self.request.user
        if (
            Validation.objects.filter(
                user=user,
                status=Validation.STARTED
            ).exists()
        ):
            raise ValidationError(
                _('Already exists a validation for the same user.')
            )

        site = Site.objects.filter(
            Q(validationgroup__isnull=True)
            | Q(validationgroup__close_date__isnull=True)
        ).exclude(validationgroup__validation__user=user).order_by('?').first()
        group = ValidationGroup.objects.get_or_create(site=site)[0]

        serializer.save(user=user, group=group)
