# Generated by Django 5.1.6 on 2025-02-22 14:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0004_roles'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='role_company', to=settings.AUTH_USER_MODEL),
        ),
    ]
