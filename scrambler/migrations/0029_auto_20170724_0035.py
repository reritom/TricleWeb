# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-23 23:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scrambler', '0028_auto_20170724_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expiringurl',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 23, 23, 35, 22, 845892, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 23, 23, 35, 22, 845892, tzinfo=utc)),
        ),
    ]
