# Generated by Django 2.1.2 on 2018-10-20 05:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accessibility', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuepage',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='Universally unique identifier'),
        ),
    ]
