# Generated by Django 5.1.6 on 2025-03-27 22:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Membreship', '0003_plans_frequency_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carateristica',
            name='plan',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='carateristicas', to='Membreship.plans'),
        ),
    ]
