#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..base.utils import RandomFileName


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
    poster = models.ImageField(
        upload_to=RandomFileName()
    )
    genres = models.ManyToManyField('Genre')
    runtime = models.PositiveIntegerField(
        _('Runtime'),
        blank=True,
        null=True
    )
    tagline = models.TextField(
        _('Tagline'),
        blank=True,
        null=True
    )
    synopsis = models.TextField(
        _('Synopsis'),
        blank=True,
        null=True
    )
    homepage = models.TextField(
        _('Homepage'),
        blank=True,
        null=True
    )
    tmdb = models.PositiveIntegerField(
        null=True
    )

    class Meta:
        ordering = ['title']
        get_latest_by = 'released'

    def __str__(self):
        return '{s.title}'.format(s=self)


class Genre(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=128
    )
    tmdb = models.PositiveIntegerField(
        null=True
    )

    def __str__(self):
        return '{s.name}'.format(s=self)


class Watchlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL
    )
    movie = models.ForeignKey(
        'Movie'
    )
    created = models.DateTimeField(
        _('Created'),
        auto_now_add=True
    )
    watched = models.DateTimeField(
        _('Watched'),
        blank=True,
        null=True
    )

    class Meta:
        permissions = (
            ('view_watchlist', _('View watchlist')),
        )

    def __str__(self):
        return '{s.movie} ({s.user})'.format(s=self)


class Resume(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL
    )
    movie = models.ForeignKey(
        'Movie'
    )
    position = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        unique_together = (
            ('user', 'movie'),
        )
        permissions = (
            ('view_resume', _('View resume')),
        )


class Rating(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL
    )
    movie = models.ForeignKey(
        'Movie'
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    stars = models.PositiveSmallIntegerField(
        default=0
    )
    comment = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        permissions = (
            ('view_rating', _('View rating')),
        )


class History(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL
    )
    movie = models.ForeignKey(
        'Movie'
    )
    date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        permissions = (
            ('view_history', _('View history')),
        )
