#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework.filters import DjangoObjectPermissionsFilter

from .. import (
    models,
    permissions,
)
from ..serializers import (
    primarykey as serializers
)


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class WatchlistViewSet(viewsets.ModelViewSet):
    queryset = models.Watchlist.objects.all()
    serializer_class = serializers.WatchlistSerializer
    filter_backends = [
        DjangoObjectPermissionsFilter,
    ]
    permission_classes = [
        permissions.DjangoObjectPermissions,
    ]


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = models.Resume.objects.all()
    serializer_class = serializers.ResumeSerializer
    filter_backends = [
        DjangoObjectPermissionsFilter,
    ]
    permission_classes = [
        permissions.DjangoObjectPermissions,
    ]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
