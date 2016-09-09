#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers


from . import models


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        extra_kwargs = {
            'url': {
                'view_name': 'web:api:movie-detail',
            }
        }


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Serie
        extra_kwargs = {
            'url': {
                'view_name': 'web:api:serie-detail',
            }
        }


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Episode
        extra_kwargs = {
            'url': {
                'view_name': 'web:api:episode-detail',
            }
        }


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        extra_kwargs = {
            'url': {
                'view_name': 'web:api:genre-detail',
            }
        }
