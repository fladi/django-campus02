#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'base/index.html'


class NotFoundView(TemplateView):
    template_name = 'base/404.html'
