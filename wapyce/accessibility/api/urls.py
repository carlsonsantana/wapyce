"""
Wapyce URL Configuration for API of accessibility app.
"""

from django.urls import path

from . import views

# pylint: disable=invalid-name
urlpatterns = [
    path('issues/', views.NewIssueAPIView.as_view(), name='new_issue'),
]
