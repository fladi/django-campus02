#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^cookies$', views.CookieView.as_view(), name='cookies'),
    url(r'^cache/expires$', views.CacheExpiresView.as_view(), name='cache/expires'),
    url(r'^cache/expires/image$', views.CacheExpiresImageView.as_view(), name='cache/expires/image'),
    url(r'^cache/etag$', views.CacheEtagView.as_view(), name='cache/etag'),
    url(r'^cache/etag/image$', views.CacheEtagImageView.as_view(), name='cache/etag/image'),
    url(r'^cache/control$', views.CacheControlView.as_view(), name='cache/control'),
    url(r'^cache/control/image$', views.CacheControlImageView.as_view(), name='cache/control/image'),
)
