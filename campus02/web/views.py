#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from six.moves import cStringIO
from PIL import ImageFont, Image, ImageDraw

from django.core.urlresolvers import reverse_lazy as reverse
from django.http import HttpResponse, HttpResponseNotModified
from django.utils.http import http_date
from django.views.generic import View
from django.views.generic.edit import FormView

from braces.views import CsrfExemptMixin

from . import forms

def get_expires(session):
    if not 'web:cache/expires' in session:
        expires = datetime.now() + timedelta(minutes=2)
        session['web:cache/expires'] = expires
    return session.get('web:cache/expires')

class CookieView(FormView):
    template_name = 'web/cookies.html'
    form_class = forms.CookieForm
    success_url = reverse('web:cookies')

    def form_valid(self, form):
        response = super(CookieView, self).form_valid(form)
        response.set_cookie(**form.cleaned_data)
        return response

    def get_context_data(self, **kwargs):
        context = super(CookieView, self).get_context_data(**kwargs)
        context['cookies'] = self.request.COOKIES
        return context

class CacheExpiresView(FormView):
    template_name = 'web/cache-expires.html'
    form_class = forms.CacheExpiresForm
    success_url = reverse('web:cache/expires')

    def form_valid(self, form):
        response = super(CacheExpiresView, self).form_valid(form)
        self.request.session['web:cache/expires'] = form.cleaned_data['expires']
        return response

    def get_initial(self):
        return {
            'expires': get_expires(self.request.session),
        }

    def get_context_data(self, **kwargs):
        context = super(CacheExpiresView, self).get_context_data(**kwargs)
        context['expires'] = get_expires(self.request.session)
        return context

class CacheExpiresImageView(View):
    font = ImageFont.truetype('/usr/share/fonts/dejavu/DejaVuSans.ttf',25)
    width = 500
    height = 100

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='image/png')
        response['Expires'] = http_date(get_expires(request.session).timestamp())
        img = Image.new('RGBA', (self.width, self.height), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        date = 'Erzeugt: {date}'.format(date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        bounds = draw.textsize(
            date,
            font=self.font
        )
        draw.text(
            ((self.width-bounds[0])/2, (self.height-bounds[1])/2),
            date,
            (255, 255, 255),
            font=self.font
        )
        img.save(response, format='PNG')
        img.close()
        return response


class CacheEtagView(FormView):
    template_name = 'web/cache-etag.html'
    form_class = forms.CacheEtagForm
    success_url = reverse('web:cache/etag')

    def form_valid(self, form):
        response = super(CacheEtagView, self).form_valid(form)
        self.request.session['web:cache/etag'] = form.cleaned_data['etag']
        self.request.session['web:cache/etag/age'] = form.cleaned_data['age']
        return response

    def get_initial(self):
        return {
            'etag': self.request.session.get('web:cache/etag', '0'),
            'age': self.request.session.get('web:cache/etag/age', 1),
        }

    def get_context_data(self, **kwargs):
        context = super(CacheEtagView, self).get_context_data(**kwargs)
        context['etag'] = self.request.session.get('web:cache/etag', '0')
        context['age'] = self.request.session.get('web:cache/etag/age', 1)
        return context


class CacheEtagImageView(CsrfExemptMixin, View):
    font = ImageFont.truetype('/usr/share/fonts/dejavu/DejaVuSans.ttf',25)
    width = 500
    height = 100

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='image/png')
        img = Image.new('RGBA', (self.width, self.height), (0, 0, 0))
        if 'web:cache/etag' in request.session:
            etag = request.session.get('web:cache/etag')
            age = request.session.get('web:cache/etag/age')
            if etag == request.META.get('HTTP_IF_NONE_MATCH', None):
                response = HttpResponseNotModified()
                response['Cache-Control'] = 'public, must-revalidate, max-age={age}'.format(age=age)
                response['ETag'] = '"{etag}"'.format(etag=etag)
                return response
            response['Cache-Control'] = 'public, must-revalidate, max-age={age}'.format(age=age)
            response['ETag'] = '"{etag}"'.format(etag=etag)
        draw = ImageDraw.Draw(img)
        date = 'Erzeugt: {date}'.format(date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        bounds = draw.textsize(
            date,
            font=self.font
        )
        draw.text(
            ((self.width-bounds[0])/2, (self.height-bounds[1])/2),
            date,
            (255, 255, 255),
            font=self.font
        )
        img.save(response, format='PNG')
        img.close()
        return response


class CacheControlView(FormView):
    template_name = 'web/cache-control.html'
    form_class = forms.CacheControlForm
    success_url = reverse('web:cache/control')

    def form_valid(self, form):
        response = super(CacheControlView, self).form_valid(form)
        self.request.session['web:cache/control'] = form.cleaned_data['control']
        return response

    def get_initial(self):
        return {
            'control': self.request.session.get('web:cache/control', ''),
        }

    def get_context_data(self, **kwargs):
        context = super(CacheControlView, self).get_context_data(**kwargs)
        context['control'] = self.request.session.get('web:cache/control', '')
        return context


class CacheControlImageView(View):
    font = ImageFont.truetype('/usr/share/fonts/dejavu/DejaVuSans.ttf',25)
    width = 500
    height = 100

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='image/png')
        img = Image.new('RGBA', (self.width, self.height), (0, 0, 0))
        if 'web:cache/control' in request.session:
            control = request.session.get('web:cache/control')
            response['Cache-Control'] = control
        draw = ImageDraw.Draw(img)
        date = 'Erzeugt: {date}'.format(date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        bounds = draw.textsize(
            date,
            font=self.font
        )
        draw.text(
            ((self.width-bounds[0])/2, (self.height-bounds[1])/2),
            date,
            (255, 255, 255),
            font=self.font
        )
        img.save(response, format='PNG')
        img.close()
        return response
