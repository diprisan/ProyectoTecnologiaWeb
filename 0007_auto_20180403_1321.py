# Generated by Django 2.0.3 on 2018-04-03 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20180331_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='ventas_totales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_hotel', models.IntegerField(default=0)),
                ('anio', models.DecimalField(decimal_places=0, max_digits=20, verbose_name='Kolichestvo characters in the teaser ')),
                ('mes', models.DecimalField(decimal_places=0, max_digits=20, verbose_name='Kolichestvo characters in the teaser ')),
                ('total', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Kolichestvo characters in the teaser ')),
                ('cant_facturas', models.DecimalField(decimal_places=0, max_digits=20, verbose_name='Kolichestvo characters in the teaser ')),
            ],
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 3, 13, 21, 5, 640725), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='fecha_eliminacion',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 3, 13, 21, 5, 640725), verbose_name='date published'),
        ),
    ]