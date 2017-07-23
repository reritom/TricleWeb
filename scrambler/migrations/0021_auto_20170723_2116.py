# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-23 20:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scrambler', '0020_auto_20170723_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expiringurl',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 23, 20, 16, 24, 996974, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 23, 21, 16, 24, 996474)),
        ),
    ]
