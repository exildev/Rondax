# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0005_remove_turno_hora_inicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='hora_inicio',
            field=models.TimeField(default='00:00'),
            preserve_default=False,
        ),
    ]
