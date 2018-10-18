"""
Views of core application.
"""

from django.shortcuts import render

# Create your views here.

def home(request):
    """
    View of home page.
    """

    return render(request, 'home.html')
