# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-23 18:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrambler', '0013_auto_20170723_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expiringurl',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 23, 19, 45, 48, 584847)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 23, 19, 45, 48, 584344)),
        ),
    ]
