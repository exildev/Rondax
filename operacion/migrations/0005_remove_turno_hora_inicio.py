# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0004_turno_hora_inicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turno',
            name='hora_inicio',
        ),
    ]
