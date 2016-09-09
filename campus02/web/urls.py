#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from rest_framework import routers

from . import (
    api,
    views,
)


router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'series', views.SerieViewSet)
router.register(r'episodes', views.EpisodeViewSet)
router.register(r'genres', views.GenreViewSet)

urlpatterns = [
    url(r'^cookies$', views.CookieView.as_view(), name='cookies'),
    url(r'^cache/expires$', views.CacheExpiresView.as_view(), name='cache/expires'),
    url(r'^cache/expires/image$', views.CacheExpiresImageView.as_view(), name='cache/expires/image'),
    url(r'^cache/etag$', views.CacheEtagView.as_view(), name='cache/etag'),
    url(r'^cache/etag/image$', views.CacheEtagImageView.as_view(), name='cache/etag/image'),
    url(r'^cache/control$', views.CacheControlView.as_view(), name='cache/control'),
    url(r'^cache/control/image$', views.CacheControlImageView.as_view(), name='cache/control/image'),
    url(r'^session$', views.SessionView.as_view(), name='session'),
    url(r'^http2$', views.Http2View.as_view(), name='http2'),
    url(r'^form-data$', views.FormDataView.as_view(), name='form-data'),
    url(r'^order$', views.OrderView.as_view(), name='order'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls, namespace='api')),
]
