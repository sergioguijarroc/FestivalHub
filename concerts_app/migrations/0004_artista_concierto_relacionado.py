# Generated by Django 4.2.11 on 2024-05-05 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concerts_app', '0003_rename_festival_concierto_concierto_festival_relacionado'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='concierto_relacionado',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='concerts_app.concierto'),
            preserve_default=False,
        ),
    ]
