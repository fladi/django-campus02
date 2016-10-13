#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import viewsets, filters

from .. import (
    models,
    permissions,
)
from ..serializers import (
   hyperlink as serializers
)
from ..filters import IsUserFilter


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    filter_backends = (
        filters.OrderingFilter,
    )
    ordering_fields = (
        'title',
        'released',
        'runtime',
    )


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    filter_backends = (
        filters.OrderingFilter,
    )
    ordering_fields = (
        'name',
    )


class WatchlistViewSet(viewsets.ModelViewSet):
    queryset = models.Watchlist.objects.all()
    serializer_class = serializers.WatchlistSerializer
    filter_backends = (
        IsUserFilter,
        filters.DjangoObjectPermissionsFilter,
    )
    permission_classes = (
        permissions.DjangoObjectPermissions,
    )


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = models.Resume.objects.all()
    serializer_class = serializers.ResumeSerializer
    filter_backends = (
        IsUserFilter,
        filters.DjangoObjectPermissionsFilter,
    )
    permission_classes = (
        permissions.DjangoObjectPermissions,
    )


class RatingViewSet(viewsets.ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
    filter_backends = (
        IsUserFilter,
        filters.DjangoObjectPermissionsFilter,
    )
    permission_classes = (
        permissions.DjangoObjectPermissions,
    )


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = models.History.objects.all()
    serializer_class = serializers.HistorySerializer
    filter_backends = (
        IsUserFilter,
        filters.DjangoObjectPermissionsFilter,
    )
    permission_classes = (
        permissions.DjangoObjectPermissions,
    )
