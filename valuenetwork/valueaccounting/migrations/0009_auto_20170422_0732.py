# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-22 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valueaccounting', '0008_auto_20170319_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='economicevent',
            name='digital_currency_tx_state',
            field=models.CharField(blank=True, choices=[(b'new', 'New'), (b'pending', 'Pending'), (b'broadcast', 'Broadcast'), (b'confirmed', 'Confirmed'), (b'external', 'External')], max_length=12, null=True, verbose_name='digital currency transaction state'),
        ),
    ]
