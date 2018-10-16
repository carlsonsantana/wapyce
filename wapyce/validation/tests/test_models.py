"""
Tests for models of validation app.
"""

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Q
from django.db.utils import IntegrityError
from django.test import TestCase

from wapyce.validation.models import Site
from wapyce.validation.models import Page
from wapyce.validation.models import Validation
from wapyce.validation.models import ValidationGroup

# Create your tests here.
class TestSite(TestCase):
    """
    Test for site model.
    """

    def tearDown(self):
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

class TestValidationGroup(TestCase):
    """
    Test for validation group model.
    """

    def setUp(self):
        self.site = Site(
            name='Site',
            base_url='http://www.example.com/',
            github_url='https://github.com/carlsonsantana/wapyce'
        )
        self.site.save()
        self.user1 = User.objects.create_user(
            username='user1',
            email='user1@github.com',
            password='user1password'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            email='user2@github.com',
            password='user2password'
        )
        self.user3 = User.objects.create_user(
            username='user3',
            email='user3@github.com',
            password='user3password'
        )

    def tearDown(self):
        groups = ValidationGroup.objects.filter(site=self.site)
        for group in groups:
            validations = Validation.objects.filter(group=group)
            for validation in validations:
                pages = Page.objects.filter(validation_site=validation)
                for page in pages:
                    page.delete()
                validation.delete()
            group.delete()
        self.site.delete()
        self.user1.delete()
        self.user2.delete()
        self.user3.delete()

    def test_normal_save(self):
        """
        Test if django persist a valid validation group object.
        """

        group = ValidationGroup(site=self.site)
        group.full_clean()
        group.save()
        self.assertEqual(
            group,
            ValidationGroup.objects.all().order_by('?').first()
        )

    def test_close_group(self):
        """
        Test if all validation are closed or canceled, when the group is
        closed.
        """

        group = ValidationGroup(site=self.site)
        group.save()

        self.assertFalse(group.is_closed())

        validation1 = Validation(group=group, user=self.user1)
        validation1.save()
        validation2 = Validation(group=group, user=self.user2)
        validation2.save()
        validation3 = Validation(group=group, user=self.user3)
        validation3.save()
        validation2.cancel_validation()
        page = Page(validation_site=validation3, page_url=self.site)
        page.save()
        validation3.finish_validation()

        group.close_group()
        validation1.refresh_from_db()
        validation2.refresh_from_db()
        validation3.refresh_from_db()

        self.assertTrue(group.is_closed())
        self.assertTrue(validation1.is_canceled())
        self.assertTrue(validation2.is_canceled())
        self.assertTrue(validation3.is_closed())

class TestValidation(TestCase):
    """
    Test for validation model.
    """

    def setUp(self):
        self.site = Site(
            name='Site',
            base_url='http://www.example.com/',
            github_url='https://github.com/carlsonsantana/wapyce'
        )
        self.site.save()
        self.user1 = User.objects.create_user(
            username='user1',
            email='user1@github.com',
            password='user1password'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            email='user2@github.com',
            password='user2password'
        )
        self.group1 = ValidationGroup(site=self.site)
        self.group1.save()
        self.group2 = ValidationGroup(site=self.site)
        self.group2.save()

    def tearDown(self):
        validations = Validation.objects.filter(
            Q(group=self.group1)
            | Q(group=self.group2)
        )
        for validation in validations:
            pages = Page.objects.filter(validation_site=validation)
            for page in pages:
                page.delete()
            validation.delete()
        self.group1.delete()
        self.group2.delete()
        self.site.delete()
        self.user1.delete()
        self.user2.delete()

    def test_normal_save(self):
        """
        Test if django persist a valid validation object.
        """

        validation1 = Validation(group=self.group1, user=self.user1)
        validation1.save()
        validation1.cancel_validation()
        validation2 = Validation(group=self.group1, user=self.user2)
        validation2.save()
        page = Page(validation_site=validation2, page_url=self.site.base_url)
        page.save()
        validation2.finish_validation()

        validation3 = Validation(group=self.group2, user=self.user1)
        validation3.save()
        validation4 = Validation(group=self.group2, user=self.user2)
        validation4.save()

        self.assertEqual(4, Validation.objects.all().count())

    def test_unique_validation_user(self):
        """
        Test unique active validation by user constraint.
        """

        with self.assertRaises(ValidationError):
            validation1 = Validation(group=self.group1, user=self.user1)
            validation1.save()
            validation2 = Validation(group=self.group2, user=self.user1)
            validation2.clean()
            validation2.save()

class TestPage(TestCase):
    """
    Test for validated page model.
    """

    def setUp(self):
        self.site = Site(
            name='Site',
            base_url='http://www.example.com/',
            github_url='https://github.com/carlsonsantana/wapyce'
        )
        self.site.save()
        self.user = User.objects.create_user(
            username='user',
            email='user@github.com',
            password='userpassword'
        )
        self.group = ValidationGroup(site=self.site)
        self.group.save()
        self.validation = Validation(group=self.group, user=self.user)
        self.validation.save()

    def tearDown(self):
        pages = Page.objects.filter(validation_site=self.validation)
        for page in pages:
            page.delete()
        self.validation.delete()
        self.group.delete()
        self.site.delete()
        self.user.delete()

    def test_normal_save(self):
        """
        Test if django persist a valid validated page object.
        """

        page = Page(
            validation_site=self.validation,
            page_url=self.site.base_url
        )
        page.clean()
        page.save()
        self.assertEqual(
            page,
            Page.objects.filter(
                validation_site=self.validation
            ).order_by('?').first()
        )

    def test_valid_page_url(self):
        """
        Test a valid page url constraint.
        """

        with self.assertRaises(ValidationError):
            page = Page(
                validation_site=self.validation,
                page_url='https://github.com/carlsonsantana/wapyce'
            )
            page.clean()
            page.save()
