# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djbraintree', '0005_auto_20171123_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btcurrentsubscription',
            name='expire_at_period_end',
            field=models.BooleanField(default=False),
        ),
    ]
