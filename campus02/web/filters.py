#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import filters


class IsUserFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=request.user)
