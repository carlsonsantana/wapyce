"""
Tests for models of validation app.
"""

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase

from wapyce.validation.models import Site

# Create your tests here.
class TestSite(TestCase):
    """
    Test for site model.
    """

    def test_unique_base_url(self):
        """
        Test unique base url constraint.
        """

        with transaction.atomic(), self.assertRaises(IntegrityError):
            site1 = Site(
                name='Site1',
                base_url='http://www.example.com/',
                github_url='https://github.com/carlsonsantana/wapyce'
            )
            site1.save()
            site2 = Site(
                name='Site2',
                base_url='http://www.example.com/',
                github_url='https://github.com/carlsonsantana/wapyce1'
            )
            site2.save()

    def test_unique_github_url(self):
        """
        Test unique github url constraint.
        """

        with transaction.atomic(), self.assertRaises(IntegrityError):
            site1 = Site(
                name='Site1',
                base_url='http://www.example1.com/',
                github_url='https://github.com/carlsonsantana/wapyce'
            )
            site1.save()
            site2=Site(
                name='Site2',
                base_url='http://www.example2.com/',
                github_url='https://github.com/carlsonsantana/wapyce'
            )
            site2.save()
