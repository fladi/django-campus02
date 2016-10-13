#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers


from .. import models


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='web:api-hl:movie-detail'
    )
    genres = serializers.HyperlinkedRelatedField(
        view_name='web:api-hl:genre-detail',
        queryset=models.Genre.objects.all(),
        many=True
    )
    class Meta:
        model = models.Movie
        exclude = ('tmdb',)
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-hl:movie-detail',
            }
        }


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='web:api-hl:genre-detail'
    )
    class Meta:
        model = models.Genre
        fields = ('url', 'name')
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-hl:genre-detail',
            }
        }


class WatchlistSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.HyperlinkedRelatedField(
        view_name='web:api-hl:movie-detail',
        queryset=models.Movie.objects.all(),
        many=False
    )
    class Meta:
        model = models.Watchlist
        exclude = ('user',)
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-hl:watchlist-detail',
            }
        }


class ResumeSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.HyperlinkedRelatedField(
        view_name='web:api-hl:movie-detail',
        queryset=models.Movie.objects.all(),
        many=False
    )
    class Meta:
        model = models.Resume
        exclude = ('user',)
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-hl:resume-detail',
            }
        }


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.HyperlinkedRelatedField(
        view_name='web:api-hl:movie-detail',
        queryset=models.Movie.objects.all(),
        many=False
    )
    class Meta:
        model = models.Rating
        exclude = ('user',)
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-hl:rating-detail',
            }
        }


class HistorySerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.HyperlinkedRelatedField(
        view_name='web:api-hl:movie-detail',
        queryset=models.Movie.objects.all(),
        many=False
    )
    class Meta:
        model = models.History
        exclude = ('user',)
        extra_kwargs = {
            'url': {
                'view_name': 'web:api-hl:history-detail',
            }
        }
