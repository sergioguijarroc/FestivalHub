# Generated by Django 4.2.11 on 2024-04-29 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festivales_app', '0003_parking'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autobus',
            options={'verbose_name_plural': 'Autobuses'},
        ),
        migrations.AlterModelOptions(
            name='parking',
            options={'verbose_name_plural': 'Parkings'},
        ),
    ]