# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0006_auto_20170502_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_user',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]