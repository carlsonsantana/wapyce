# Generated by Django 2.1.2 on 2018-10-18 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('validation', '0005_auto_20181016_0414'),
    ]

    operations = [
        migrations.CreateModel(
            name='GithubIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Number of GitHub issue')),
                ('created_at', models.DateTimeField(verbose_name='Created at')),
                ('validation_site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='validation.Validation', verbose_name='Validation')),
            ],
            options={
                'verbose_name': 'GitHub issue',
            },
        ),
    ]