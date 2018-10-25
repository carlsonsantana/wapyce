"""
Views of validation application.
"""

from django.views.generic import DetailView
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

class ValidationDetailView(DetailView):
    """
    View to detail the complete validation.
    """

    queryset = Validation.objects.filter(
        status=Validation.FINISHED
    ).select_related('site').select_related('user')
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
