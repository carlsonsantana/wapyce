"""
Serializers of API validation app.
"""

from rest_framework import serializers

from wapyce.validation.models import Validation

class ValidationSerializer(serializers.ModelSerializer):
    """
    The ValidationSerializer class is a serializer of Validation model.
    """

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    group = serializers.SlugRelatedField(
        read_only=True,
        slug_field='uuid'
    )

    class Meta:
        """
        Metadata class of validation serializer.
        """

        model = Validation
        fields = ('uuid', 'group', 'user', 'start_date', 'end_date', 'status')
        read_only_fields = ('end_date', 'status')
