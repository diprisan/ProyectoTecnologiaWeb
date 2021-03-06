# Generated by Django 2.0.3 on 2018-04-04 02:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20180403_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 3, 21, 37, 43, 874155), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='fecha_eliminacion',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 3, 21, 37, 43, 874155), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='ventas_totales',
            name='anio',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='ventas_totales',
            name='cant_facturas',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='ventas_totales',
            name='cliente',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='ventas_totales',
            name='mes',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='ventas_totales',
            name='normal',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='ventas_totales',
            name='salon',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='ventas_totales',
            name='suit',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='ventas_totales',
            name='total',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]
