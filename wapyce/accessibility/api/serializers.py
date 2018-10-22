"""
Serializers of API accessibility app.
"""

from rest_framework import serializers

from wapyce.accessibility.models import IssueCode
from wapyce.accessibility.models import IssuePage
from wapyce.validation.models import Page

class IssuePageSerializer(serializers.ModelSerializer):
    """
    The IssuePageSerializer class is a serializer of IssuePage model.
    """

    page = serializers.SlugRelatedField(
        queryset=Page.objects.all(),
        slug_field='uuid',
    )
    code = serializers.SlugRelatedField(
        queryset=IssueCode.objects.all(),
        slug_field='code',
    )

    class Meta:
        """
        Metadata class of issue page serializer.
        """

        model = IssuePage
        fields = (
            'uuid',
            'page',
            'code',
            'context',
            'message',
            'selector',
            'issue_type',
        )
