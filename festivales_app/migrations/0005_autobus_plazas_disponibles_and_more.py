# Generated by Django 4.2.11 on 2024-05-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivales_app', '0004_alter_autobus_options_alter_parking_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='autobus',
            name='plazas_disponibles',
            field=models.PositiveIntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parking',
            name='plazas_disponibles',
            field=models.PositiveIntegerField(default=30),
            preserve_default=False,
        ),
    ]