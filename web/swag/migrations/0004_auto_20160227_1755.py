# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 17:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swag', '0003_auto_20160227_1610'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShowEvent',
            new_name='Episode',
        ),
        migrations.RenameModel(
            old_name='TeamEvent',
            new_name='Game',
        ),
    ]
