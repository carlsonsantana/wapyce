"""
Wapyce URL Configuration for core app.
"""

from django.urls import include
from django.urls import path

from . import views

# pylint: disable=invalid-name
urlpatterns = [
    path('', views.home, name='home'),
    path('donate/', views.donate, name='donate'),
    path('account/login/', views.login, name='login'),
    path('account/logout/', views.logout_view, name='logout'),
    path('account/settings/', views.settings_view, name='settings'),
    path(
      'account/settings/new_token',
      views.new_user_token,
      name='new_user_token'
    ),
    path('oauth/', include('social_django.urls', namespace='social')),
]
