# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 19:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20160908_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='name',
            new_name='title',
        ),
    ]
