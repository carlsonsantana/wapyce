"""
Wapyce URL Configuration for validation app.
"""

from django.urls import path

from .views import ValidationDetailView
from .views import ValidationListView

# pylint: disable=invalid-name
urlpatterns = [
    path(
        'validations/',
        ValidationListView.as_view(),
        name='list_validations'
    ),
    path(
        'validations/<uuid:uuid>/',
        ValidationDetailView.as_view(),
        name='detail_validation'
    ),
]
