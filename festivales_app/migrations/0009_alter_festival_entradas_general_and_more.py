# Generated by Django 5.0.6 on 2024-05-23 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivales_app', '0008_alter_festival_precio_entrada_general_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festival',
            name='entradas_general',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='entradas_oro',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='entradas_platino',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='precio_entrada_general',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='precio_entrada_oro',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='precio_entrada_platino',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]