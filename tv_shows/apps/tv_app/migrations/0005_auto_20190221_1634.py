# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-22 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_app', '0004_auto_20190221_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='release_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]