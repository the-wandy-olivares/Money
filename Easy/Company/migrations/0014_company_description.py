# Generated by Django 5.1.6 on 2025-02-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0013_more_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, default='Préstamos rápidos y seguros', null=True),
        ),
    ]
