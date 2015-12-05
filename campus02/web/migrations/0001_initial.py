# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('zip_code', models.PositiveSmallIntegerField()),
                ('city', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('product', models.CharField(max_length=256)),
                ('amount', models.PositiveSmallIntegerField()),
                ('delivery', models.CharField(max_length=256)),
                ('gift', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='')),
                ('comment', models.TextField(blank=True)),
                ('student', models.OneToOneField(to='base.Student')),
            ],
        ),
    ]
