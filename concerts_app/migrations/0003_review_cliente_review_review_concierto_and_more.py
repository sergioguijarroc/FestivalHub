# Generated by Django 4.2.9 on 2024-01-24 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concerts_app', '0002_notificacion_review'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='cliente_review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='concierto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concerts_app.concierto'),
        ),
        migrations.AddField(
            model_name='notificacion',
            name='cliente_notificacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
