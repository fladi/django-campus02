#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^web/', include('campus02.web.urls', namespace='web')),
    url(r'^', include('campus02.base.urls', namespace='base')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
        url(
            r'^__debug__/',
            include(debug_toolbar.urls)
        )
    )
    urlpatterns.append(
        url(
            r'^media/(?P<path>.*)$',
            serve,
            {
                'document_root': settings.MEDIA_ROOT,
            }
        )
    )
    urlpatterns.append(
        url(
            r'^static/(?P<path>.*)$',
            serve,
            {
                'document_root': settings.STATIC_ROOT,
            }
        ),
    )
