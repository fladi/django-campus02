#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin

from reversion.admin import VersionAdmin

from . import models


@admin.register(models.Order)
class OrderAdmin(VersionAdmin):
    list_display = ('student',)


@admin.register(models.Movie)
class MovieAdmin(VersionAdmin):
    list_display = ('title',)


class EpisodeInline(admin.TabularInline):
    model = models.Episode


@admin.register(models.Serie)
class SerieAdmin(VersionAdmin):
    list_display = ('title',)
    inlines = [
        EpisodeInline,
    ]


@admin.register(models.Genre)
class SerieAdmin(VersionAdmin):
    list_display = ('name',)
