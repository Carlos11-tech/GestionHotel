# Generated by Django 5.0.6 on 2024-06-05 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitacion',
            name='factura',
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='numero',
            field=models.IntegerField(unique=True),
        ),
    ]
