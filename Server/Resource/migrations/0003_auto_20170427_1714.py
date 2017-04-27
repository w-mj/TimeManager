# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0002_auto_20170426_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_updatetime',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='school_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
