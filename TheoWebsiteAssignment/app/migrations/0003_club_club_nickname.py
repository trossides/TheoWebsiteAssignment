# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180411_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='club_nickname',
            field=models.CharField(default=1, help_text='The Nickname of the Club.', max_length=20),
            preserve_default=False,
        ),
    ]
