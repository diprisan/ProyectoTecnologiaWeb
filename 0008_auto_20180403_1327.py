# Generated by Django 2.0.3 on 2018-04-03 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20180403_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 3, 13, 26, 59, 992695), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='fecha_eliminacion',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 3, 13, 26, 59, 992695), verbose_name='date published'),
        ),
    ]
