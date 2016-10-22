#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from rest_framework import routers

from . import (
    views,
)
from .views import (
    hyperlink,
    primarykey,
)



api_hl = routers.DefaultRouter()
api_hl.register(r'movies', hyperlink.MovieViewSet)
api_hl.register(r'genres', hyperlink.GenreViewSet)
api_hl.register(r'watchlists', hyperlink.WatchlistViewSet)
api_hl.register(r'resumes', hyperlink.ResumeViewSet)
api_hl.register(r'ratings', hyperlink.RatingViewSet)
api_hl.register(r'history', hyperlink.HistoryViewSet)

api_pk = routers.DefaultRouter()
api_pk.register(r'movies', primarykey.MovieViewSet)
api_pk.register(r'genres', primarykey.GenreViewSet)
api_pk.register(r'watchlists', primarykey.WatchlistViewSet)
api_pk.register(r'resumes', primarykey.ResumeViewSet)
api_pk.register(r'ratings', primarykey.RatingViewSet)
api_pk.register(r'history', hyperlink.HistoryViewSet)

urlpatterns = [
    url(
        r'^cookies$',
        views.CookieView.as_view(),
        name='cookies'
    ),
    url(
        r'^cache/expires$',
        views.CacheExpiresView.as_view(),
        name='cache/expires'
    ),
    url(
        r'^cache/expires/image$',
        views.CacheExpiresImageView.as_view(),
        name='cache/expires/image'
    ),
    url(
        r'^cache/etag$',
        views.CacheEtagView.as_view(),
        name='cache/etag'
    ),
    url(
        r'^cache/etag/image$',
        views.CacheEtagImageView.as_view(),
        name='cache/etag/image'
    ),
    url(
        r'^cache/control$',
        views.CacheControlView.as_view(),
        name='cache/control'
    ),
    url(
        r'^cache/control/image$',
        views.CacheControlImageView.as_view(),
        name='cache/control/image'
    ),
    url(
        r'^session$',
        views.SessionView.as_view(),
        name='session'
    ),
    url(
        r'^http2$',
        views.Http2View.as_view(),
        name='http2'
    ),
    url(
        r'^form-data$',
        views.FormDataView.as_view(),
        name='form-data'
    ),
    url(
        r'^order$',
        views.OrderView.as_view(),
        name='order'
    ),
    url(
        r'^auth$',
        views.AuthView.as_view(),
        name='auth'
    ),
    url(
        r'^auth/secure$',
        views.AuthSecureView.as_view(),
        name='auth/secure'
    ),
    url(
        r'^mime/(?P<type>.*)?$',
        views.MimeView.as_view(),
        name='mime'
    ),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    url(
        r'^api-hl/',
        include(api_hl.urls, namespace='api-hl')
    ),
    url(
        r'^api-pk/',
        include(api_pk.urls, namespace='api-pk')
    ),
]
