# Generated by Django 5.1.6 on 2025-02-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0015_remove_configuration_interes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='interes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='porcentaje_mora',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
