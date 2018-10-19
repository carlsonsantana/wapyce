"""
Views of core application.
"""

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here.

def home(request):
    """
    View of home page.
    """

    return render(request, 'home.html')

def login(request):
    """
    View of login page.
    """

    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    """
    View to logout user.
    """

    logout(request)
    return redirect('home')
