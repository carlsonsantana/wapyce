"""
Views of API accessibility application.
"""

from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView

from wapyce.accessibility.models import IssueCode
from wapyce.accessibility.models import IssuePage
from .serializers import IssuePageSerializer

class NewIssueAPIView(CreateAPIView):
    """
    View of API to register a new issue of page validated.
    """

    queryset = IssuePage.objects.all()
    serializer_class = IssuePageSerializer

    def perform_create(self, serializer):
        """
        Register a new issue of page validated.
        """

        validation = serializer.validated_data['page'].validation_site
        if (validation.user != self.request.user) or (not validation.started):
            raise PermissionDenied()
        code = IssueCode.objects.get_or_create(
            code=serializer.validated_data['code']
        )

        serializer.save(code=code[0])
