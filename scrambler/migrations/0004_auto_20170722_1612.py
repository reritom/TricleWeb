# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-22 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrambler', '0003_delete_tempurl'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserScrambleInfo',
            new_name='Profile',
        ),
    ]
