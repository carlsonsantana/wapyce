"""
Create admin CRUDs for validation app.
"""

from django.contrib import admin

from .models import Site

# Register your models here.

class SiteAdmin(admin.ModelAdmin):
    """
    Create admin CRUD for Site model.
    """

    list_display = ('name', 'base_url', 'github_url')

admin.site.register(Site, SiteAdmin)
