# Generated by Django 5.1.6 on 2025-03-23 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inversion', '0003_alter_inversion_company_alter_inversion_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inversion',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
