#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pkz', 'first_name', 'last_name',)
