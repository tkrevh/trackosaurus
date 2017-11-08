# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recordedevent',
            options={'ordering': ['-date_created'], 'verbose_name': 'Recorded Event', 'verbose_name_plural': 'Recorded Events'},
        ),
        migrations.AlterField(
            model_name='campaignevent',
            name='type',
            field=models.PositiveIntegerField(choices=[(1, b'E-Commerce'), (2, b'SaaS'), (99, b'Other')], default=99),
        ),
    ]