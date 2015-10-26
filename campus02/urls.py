#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^web/', include('campus02.web.urls', namespace='web')),
    url(r'^', include('campus02.base.urls', namespace='base')),
)
