# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0005_auto_20170502_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_user',
            name='privilege',
            field=models.CharField(choices=[('owner', 'owner'), ('master', 'master'), ('member', 'member')], max_length=20),
        ),
    ]
