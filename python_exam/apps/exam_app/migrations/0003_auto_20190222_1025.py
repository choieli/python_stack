# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-22 18:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0002_auto_20190222_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fisrt_name',
            new_name='first_name',
        ),
    ]
