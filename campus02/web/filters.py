#!/usr/bin/python
# -*- coding: utf-8 -*-

from django_filters import NumberFilter, DateFilter
from rest_framework import filters

from . import models


class IsUserFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=request.user)


class MovieFilter(filters.FilterSet):
    min_runtime = NumberFilter(name='runtime', lookup_expr='gte')
    max_runtime = NumberFilter(name='runtime', lookup_expr='lte')
    min_released = DateFilter(name='released', lookup_expr='gte')
    max_released = DateFilter(name='released', lookup_expr='lte')

    class Meta:
        model = models.Movie
        fields = {
            'title': ['exact', 'icontains'],
            'genres': ['exact'],
            'runtime': ['exact', 'gt', 'lt'],
            'released': ['exact', 'gt', 'lt'],
        }
