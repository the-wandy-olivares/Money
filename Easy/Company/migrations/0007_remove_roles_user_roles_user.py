# Generated by Django 5.1.6 on 2025-02-22 15:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0006_remove_roles_user_roles_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roles',
            name='user',
        ),
        migrations.AddField(
            model_name='roles',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='role_company', to=settings.AUTH_USER_MODEL),
        ),
    ]
