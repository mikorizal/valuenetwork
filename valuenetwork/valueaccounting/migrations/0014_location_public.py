# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-05-02 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valueaccounting', '0013_auto_20180530_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]