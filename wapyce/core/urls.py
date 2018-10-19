"""
Wapyce URL Configuration for core app.
"""

from django.urls import include
from django.urls import path

from . import views

# pylint: disable=invalid-name
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
]
