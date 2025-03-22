# Generated by Django 5.1.6 on 2025-03-22 22:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0020_alter_configuration_color_enfasis'),
        ('Credit', '0016_credit_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='company',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Compañia', to='Company.company', verbose_name='Compañia asociada al credito'),
        ),
    ]
