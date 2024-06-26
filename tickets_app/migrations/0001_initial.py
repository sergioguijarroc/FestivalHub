# Generated by Django 5.0.6 on 2024-05-23 08:51

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('festivales_app', '0008_alter_festival_precio_entrada_general_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaAutobus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_tickets', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('autobus_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festivales_app.autobus')),
                ('cliente_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reservas de Autobuses',
            },
        ),
        migrations.CreateModel(
            name='ReservaFestival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_tickets', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_entrada', models.CharField(max_length=50)),
                ('cliente_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('festival_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festivales_app.festival')),
            ],
            options={
                'verbose_name_plural': 'Reservas de Festivales',
            },
        ),
        migrations.CreateModel(
            name='ReservaParking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_tickets', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parking_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festivales_app.parking')),
            ],
            options={
                'verbose_name_plural': 'Reservas de Parkings',
            },
        ),
    ]
