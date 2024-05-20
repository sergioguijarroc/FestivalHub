# Generated by Django 4.2.11 on 2024-04-04 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('festivales_app', '0002_autobus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion_parking', models.CharField(max_length=255)),
                ('capacidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('festival_relacionado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festivales_app.festival')),
            ],
        ),
    ]
