# Generated by Django 5.1.6 on 2025-02-17 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Credit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='metodo',
            field=models.CharField(choices=[('Frances', 'Aleman'), ('Americano', 'Fijo')], max_length=50),
        ),
    ]
