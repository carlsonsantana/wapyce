"""
Create admin CRUDs for accessibility app.
"""

from django.contrib import admin

from .models import IssueCode

# Register your models here.

admin.site.register(IssueCode)
