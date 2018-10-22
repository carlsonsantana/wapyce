"""
Wapyce URL Configuration for API of validation app.
"""

from django.urls import path

from . import views

# pylint: disable=invalid-name
urlpatterns = [
    path(
        'validations/',
        views.NewValidationAPIView.as_view(),
        name='new_validation'
    ),
    path(
        'validations/<uuid:uuid>/cancel_validation/',
        views.CancelValidationAPIView.as_view(),
        name='cancel_validation'
    ),
    path(
        'validations/<uuid:uuid>/finish_validation/',
        views.FinishValidationAPIView.as_view(),
        name='finish_validation'
    ),
    path('pages/', views.NewPageAPIView.as_view(), name='new_page'),
]
