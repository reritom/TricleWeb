# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-25 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrambler', '0035_auto_20170725_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyledger',
            name='date',
            field=models.DateTimeField(default=0, unique=True),
        ),
    ]
