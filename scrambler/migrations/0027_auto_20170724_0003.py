# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-23 23:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scrambler', '0026_auto_20170723_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expiringurl',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 23, 23, 3, 36, 386057, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 23, 23, 3, 36, 385556, tzinfo=utc)),
        ),
    ]
