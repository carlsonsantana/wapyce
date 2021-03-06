# Generated by Django 2.1.2 on 2018-10-29 05:33

from django.db import migrations


def remove_linebreaks_context(apps, schema_editor):
    IssuePage = apps.get_model('accessibility', 'IssuePage')
    for issue in IssuePage.objects.all():
        issue.context = issue.context.replace('\n', ' ')
        issue.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accessibility', '0004_auto_20181024_1744'),
    ]

    operations = [
        migrations.RunPython(
            remove_linebreaks_context,
            migrations.RunPython.noop
        )
    ]
