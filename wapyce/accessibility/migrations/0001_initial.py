# Generated by Django 2.1.2 on 2018-10-18 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('validation', '0005_auto_20181016_0414'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True, verbose_name='Issue code')),
            ],
            options={
                'verbose_name': 'Issue code',
            },
        ),
        migrations.CreateModel(
            name='IssuePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=255, verbose_name='Context')),
                ('message', models.CharField(max_length=255, verbose_name='Message')),
                ('selector', models.CharField(max_length=100, verbose_name='Selector')),
                ('issue_type', models.IntegerField(choices=[(1, 'Error'), (2, 'Warning'), (3, 'Notice')], verbose_name='Type')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accessibility.IssueCode', verbose_name='Issue code')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='validation.Page', verbose_name='Page URL')),
            ],
            options={
                'verbose_name': 'Issue of page',
            },
        ),
    ]
