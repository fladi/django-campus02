#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin

from reversion.admin import VersionAdmin
from guardian.admin import GuardedModelAdmin

from . import models


@admin.register(models.Order)
class OrderAdmin(VersionAdmin):
    list_display = ('student',)


@admin.register(models.Movie)
class MovieAdmin(VersionAdmin):
    list_display = ('title', 'released', 'runtime', 'tmdb')
    search_fields = ('title', 'tmdb')


@admin.register(models.Genre)
class GenreAdmin(VersionAdmin):
    list_display = ('name', 'tmdb')
    search_fields = ('name', 'tmdb')


@admin.register(models.Watchlist)
class WatchlistAdmin(GuardedModelAdmin):
    list_display = ('user', 'movie')


@admin.register(models.History)
class HistoryAdmin(GuardedModelAdmin):
    list_display = ('user', 'movie', 'date')
