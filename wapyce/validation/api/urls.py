"""
Wapyce URL Configuration for API of validation app.
"""

from django.urls import path

from . import views

# pylint: disable=invalid-name
urlpatterns = [
    path(
        'new_validation/',
        views.NewValidationAPIView.as_view(),
        name='new_validation'
    ),
]
