#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers


from .. import models


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        exclude = ('tmdb',)
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-pk:movie-detail',
            }
        }


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        exclude = ('tmdb',)
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-pk:genre-detail',
            }
        }


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Watchlist
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-pk:watchlist-detail',
            }
        }


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resume
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-pk:resume-detail',
            }
        }


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-pk:rating-detail',
            }
        }
