# Generated by Django 3.0.7 on 2024-01-03 16:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flow', '0001_initial'),
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Autorization',
            new_name='Authorization',
        ),
    ]
