#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin

from reversion.admin import VersionAdmin

from . import models


@admin.register(models.Order)
class OrderAdmin(VersionAdmin):
    list_display = ('student',)
