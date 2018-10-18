"""
Wapyce URL Configuration for core app.
"""

from django.urls import path

from . import views

# pylint: disable=invalid-name
urlpatterns = [
    path('', views.home, name='home')
]
