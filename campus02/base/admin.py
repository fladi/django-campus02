#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


class CourseInline(admin.TabularInline):
    model = models.Course


class InscriptionInline(admin.TabularInline):
    model = models.Student.courses.through


@admin.register(models.Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('year', 'semester',)
    inlines = [
        CourseInline,
    ]


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    inlines = [
        InscriptionInline,
    ]


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pkz', 'first_name', 'last_name',)
    inlines = [
        InscriptionInline,
    ]
