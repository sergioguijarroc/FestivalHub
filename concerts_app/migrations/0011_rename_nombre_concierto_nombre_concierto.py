# Generated by Django 4.2.13 on 2024-06-04 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concerts_app', '0010_remove_artista_concierto_relacionado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concierto',
            old_name='nombre',
            new_name='nombre_concierto',
        ),
    ]
