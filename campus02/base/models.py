#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Semester(models.Model):
    YEAR_CHOICES = map(lambda x: (x, x), range(2014, (datetime.now().year+1)))
    SUMMER = 'SS'
    WINTER = 'WS'
    SEMESTER_CHOICES = (
        (WINTER, _('Winter')),
        (SUMMER, _('Summer')),
    )
    year = models.PositiveIntegerField(
        _('Year'),
        choices=YEAR_CHOICES,
        default=datetime.now().year
    )
    semester = models.CharField(
        _('Semester'),
        max_length=2,
        choices=SEMESTER_CHOICES,
        default=SUMMER if datetime.now().month in range(3, 8) else WINTER
    )

    def __str__(self):
        return '{s.semester}{s.year}'.format(s=self)


class Course(models.Model):
    name = models.CharField(
        max_length=256
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    semester = models.ForeignKey(
        'Semester'
    )

    def __str__(self):
        return '{s.name} ({s.semester})'.format(s=self)


class Student(models.Model):
    pkz = models.PositiveIntegerField(
        _('Personal Identification Number'),
        primary_key=True
    )
    title = models.CharField(
        _('Title'),
        blank=True,
        null=True,
        max_length=64
    )
    first_name = models.CharField(
        _('First name'),
        max_length=128
    )
    last_name = models.CharField(
        _('Last name'),
        max_length=128
    )
    courses = models.ManyToManyField('Course')

    def __str__(self):
        return '{s.last_name} {s.first_name} ({s.pkz})'.format(s=self)
