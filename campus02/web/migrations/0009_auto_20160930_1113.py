# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20160929_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(blank=True, null=True, verbose_name='Synopsis'),
        ),
    ]
