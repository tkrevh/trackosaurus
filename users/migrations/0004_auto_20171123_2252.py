# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 21:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_subscribers_limit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('can_access_advanced_configuration', 'Can user access advanced configuration'), ('can_segment_notifications', 'Can user segment notifications'), ('can_use_autoresponder', 'Can user use autoresponder'), ('can_use_timed_messages', 'Can user use timed messages'), ('can_use_advanced_triggers', 'Can user use advanced triggers'))},
        ),
    ]
