# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrambler', '0036_auto_20170725_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='expiringurl',
            name='down_count',
            field=models.IntegerField(default=0),
        ),
    ]
