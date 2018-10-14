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

    def tearDown(self):
        """
        Delete all saved site.
        """

        sites = Site.objects.all()
        for site in sites:
            site.delete()

    def test_normal_save(self):
        """
        Test if django persist a valid site object.
        """

        site = Site(
            name='Site',
            base_url='http://www.example.com/',
            github_url='https://github.com/carlsonsantana/wapyce'
        )
        site.full_clean()
        site.save()
        self.assertEqual(site, Site.objects.all().order_by('?').first())

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
            site2 = Site(
                name='Site2',
                base_url='http://www.example2.com/',
                github_url='https://github.com/carlsonsantana/wapyce'
            )
            site2.save()

    def test_valid_github_url(self):
        """
        Test if django persists a invalid github url.
        """

        with self.assertRaises(ValidationError):
            site = Site(
                name='Site',
                base_url='http://www.example.com/',
                github_url='https://www.w3.org/TR/WCAG20/'
            )
            site.full_clean()
            site.save()
