# Generated by Django 4.2.11 on 2024-05-05 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concerts_app', '0005_alter_concierto_artista_concierto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concierto',
            name='artista_concierto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concerts_app.artista'),
        ),
    ]