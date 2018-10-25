"""
Notify the owner of repository of accessibility errors found, through Github
issues.
"""

from django.conf import settings
from django.core.management.base import BaseCommand
from django.template.loader import get_template
from django.utils.translation import gettext as _

from github import Github

from wapyce.accessibility.models import IssuePage
from wapyce.notifier.models import GithubIssue
from wapyce.validation.models import Page
from wapyce.validation.models import Validation


class Command(BaseCommand):
    """
    The Command class notify the owner of repository of accessibility errors
    found, through Github issues.
    """

    help = 'Notify the owner of repository of errors found.'

    def handle(self, *args, **options):
        github_connection = Github(settings.GITHUB_PERSONAL_ACCESS_TOKEN)
        template = get_template('notifier/github_issue.md')
        validations = Validation.objects.filter(
            status=Validation.FINISHED,
            githubissue__isnull=True,
        ).select_related('site').select_related('user')
        for validation in validations:
            if (
                IssuePage.objects.filter(
                    page__validation_site=validation
                ).exists()
            ):
                repo = github_connection.get_repo(validation.site.name)

                pages = Page.objects.filter(
                    validation_site=validation
                ).prefetch_related(
                    'issuepage_set'
                ).prefetch_related('issuepage_set__code')

                issue = repo.create_issue(
                    title=_('Accessibility errors found in your template'),
                    body=template.render({
                        'validation': validation,
                        'pages': pages
                    }).replace('\n\n', '\n')
                )
                GithubIssue.objects.create(
                    validation_site=validation,
                    number=issue.number,
                    created_at=issue.created_at,
                )
                self.stdout.write(self.style.SUCCESS(_(
                    'Create the issue #{}({}) of validation {}.'.format(
                        issue.id,
                        issue.html_url,
                        validation.uuid
                    )
                )))
