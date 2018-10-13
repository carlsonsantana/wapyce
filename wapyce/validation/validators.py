"""
The validators of validation app.
"""

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def validate_github_url(value):
    """
    Raise a ValidationError if the value is not a github url.
    """

    if not (
        value.startswith('https://www.github.com/')
        or value.startswith('https://github.com/')
    ):
        raise ValidationError(_('This value is not a Github valid URL.'))
