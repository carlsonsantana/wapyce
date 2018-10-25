"""
Views of validation application.
"""

from django.views.generic import ListView

from .models import Validation

class ValidationListView(ListView):
    """
    View to list finished validations.
    """

    queryset = Validation.objects.filter(
        status=Validation.FINISHED
    ).select_related('site').select_related('user').order_by('-end_date')
    paginate_by = 20
