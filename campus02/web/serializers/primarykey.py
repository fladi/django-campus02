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
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = models.Watchlist
        exclude = ('user',)
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-pk:watchlist-detail',
            }
        }


class ResumeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = models.Resume
        exclude = ('user',)
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-pk:resume-detail',
            }
        }


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = models.Rating
        exclude = ('user',)
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-pk:rating-detail',
            }
        }


class HistorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = models.History
        exclude = ('user',)
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-pk:history-detail',
            }
        }
