#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Order(models.Model):
    student = models.OneToOneField('base.Student')
    first_name = models.CharField(max_length=256, blank=False)
    last_name = models.CharField(max_length=256, blank=False)
    address = models.CharField(max_length=256, blank=False)
    zip_code = models.PositiveSmallIntegerField(blank=False)
    city = models.CharField(max_length=256, blank=False)
    email = models.EmailField(blank=False)
    product = models.CharField(max_length=256, blank=False)
    amount = models.PositiveSmallIntegerField(blank=False)
    delivery = models.CharField(max_length=256, blank=False)
    gift = models.BooleanField(default=False, blank=False)
    image = models.ImageField()
    comment = models.TextField(blank=True)


class Movie(models.Model):
    title = models.CharField(
        _('Movie'),
        max_length=256
    )
    released = models.DateField(
        _('Release date')
    )
    poster = models.ImageField()
    genres = models.ManyToManyField('Genre')
    synopsis = models.TextField(
        _('Synopsis')
    )

    def __str__(self):
        return '{s.title}'.format(s=self)


class Serie(models.Model):
    title = models.CharField(
        _('Movie'),
        max_length=256
    )
    poster = models.ImageField()
    genres = models.ManyToManyField('Genre')
    synopsis = models.TextField(
        _('Synopsis')
    )

    def __str__(self):
        return '{s.title}'.format(s=self)


class Episode(models.Model):
    title = models.CharField(
        _('Movie'),
        max_length=256
    )
    serie = models.ForeignKey(
        'Serie'
    )
    number = models.PositiveIntegerField(
        _('Number')
    )
    released = models.DateField(
        _('Release date')
    )
    poster = models.ImageField()
    synopsis = models.TextField(
        _('Synopsis')
    )

    def __str__(self):
        return '{s.title}'.format(s=self)


class Genre(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=128
    )

    def __str__(self):
        return '{s.name}'.format(s=self)
