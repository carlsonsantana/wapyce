"""
Serializers of API validation app.
"""

from rest_framework import serializers

from wapyce.validation.models import Page
from wapyce.validation.models import Validation
from wapyce.validation.models import ValidationGroup

class ValidationGroupSerializer(serializers.ModelSerializer):
    """
    The ValidationGroupSerializer class is a serializer of ValidationGroup
    model.
    """

    site = serializers.SlugRelatedField(read_only=True, slug_field='base_url')

    class Meta:
        """
        Metadata class of validation group serializer.
        """

        model = ValidationGroup
        fields = ('uuid', 'site')

class ValidationSerializer(serializers.ModelSerializer):
    """
    The ValidationSerializer class is a serializer of Validation model.
    """

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    group = ValidationGroupSerializer(read_only=True)

    class Meta:
        """
        Metadata class of validation serializer.
        """

        model = Validation
        fields = ('uuid', 'group', 'user', 'start_date', 'end_date', 'status')
        read_only_fields = ('end_date', 'status')

class PageSerializer(serializers.ModelSerializer):
    """
    The PageSerializer class is a serializer of Page model.
    """

    validation_site = serializers.SlugRelatedField(
        queryset=Validation.objects.all(),
        slug_field='uuid'
    )

    class Meta:
        """
        Metadata class of page serializer.
        """

        model = Page
        fields = ('uuid', 'validation_site', 'page_url')
