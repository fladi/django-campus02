#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^web/', include('campus02.web.urls', namespace='web')),
    url(r'^', include('campus02.base.urls', namespace='base')),
)
