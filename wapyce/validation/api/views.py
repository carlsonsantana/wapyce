"""
Views of API validation application.
"""

from django.db.models import Q
from django.utils.translation import gettext as _

from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView

from wapyce.validation.models import Site
from wapyce.validation.models import Validation
from wapyce.validation.models import Page
from .serializers import ValidationSerializer
from .serializers import PageSerializer

class NewValidationAPIView(CreateAPIView):
    """
    View of API to register the start of validation of user.
    """

    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer

    def perform_create(self, serializer):
        """
        Register the start of validation of user, if they not has a validation
        started.
        """

        user = self.request.user
        query = Validation.objects.filter(user=user, status=Validation.STARTED)
        if query.exists():
            validation = query.first()
            validation.cancel_validation()

        site = Site.objects.filter(
            Q(validation__isnull=True)
            | Q(validation__status=Validation.CANCELED)
        ).filter(status=Site.ACTIVE).order_by('?').first()

        serializer.save(user=user, site=site)

class CancelValidationAPIView(UpdateAPIView):
    """
    View of API to cancel the validation of user.
    """

    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer
    lookup_field = 'uuid'

    def perform_update(self, serializer):
        """
        Cancel the validation of user, if the user has a validation started.
        """

        query = Validation.objects.filter(
            user=self.request.user,
            status=Validation.STARTED
        )
        if not query.exists():
            raise ValidationError(_('The user not has a validation started.'))

        validation = query.first()
        validation.cancel_validation()
        serializer.data['end_date'] = validation.end_date
        serializer.data['status'] = validation.status

class FinishValidationAPIView(UpdateAPIView):
    """
    View of API to finish the validation of user.
    """

    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer
    lookup_field = 'uuid'

    def perform_update(self, serializer):
        """
        Finish the validation of user, if the user has a validation started.
        """

        query = Validation.objects.filter(
            user=self.request.user,
            status=Validation.STARTED
        )
        if not query.exists():
            raise ValidationError(_('The user not has a validation started.'))

        validation = query.first()
        validation.finish_validation()
        serializer.data['end_date'] = validation.end_date
        serializer.data['status'] = validation.status

class NewPageAPIView(CreateAPIView):
    """
    View of API to register the page of validation of user.
    """

    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def perform_create(self, serializer):
        """
        Register the page of validation of user.
        """

        validation = serializer.validated_data['validation_site']
        if (validation.user != self.request.user) or (not validation.started):
            raise PermissionDenied()
        base_url = validation.site.base_url
        page_url = serializer.validated_data['page_url']
        if not page_url.startswith(base_url):
            raise ValidationError(
                _('The page URL must starts with "{}".').format(base_url)
            )

        serializer.save()
