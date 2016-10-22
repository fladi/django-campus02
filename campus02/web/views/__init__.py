#!/usr/bin/python
# -*- coding: utf-8 -*-

from base64 import b64decode
from datetime import datetime, timedelta
from collections import OrderedDict
from random import SystemRandom
from PIL import ImageFont, Image, ImageDraw
from string import digits

from django.core.urlresolvers import reverse_lazy as reverse
from django.http import HttpResponse, HttpResponseNotModified
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import http_date
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from braces.views import CsrfExemptMixin

from campus02.base import models as base_models
from .. import (
    forms,
    models,
)


def get_expires(session):
    if 'web:cache/expires' not in session:
        expires = datetime.now() + timedelta(minutes=2)
        session['web:cache/expires'] = expires
    return session.get('web:cache/expires')


class BasicAuthMixin(object):
    error_template_name = None
    realm = 'Realm'

    def get_error_template_name(self):
        return self.error_template_name

    def get_realm(self):
        return self.realm

    def get_error_context(self, request):
        return {}

    def authenticate(self, username, password):
        return False

    def dispatch(self, request, *args, **kwargs):
        header = request.META.get('HTTP_AUTHORIZATION', None)
        if header:
            auth = header.split()
            if len(auth) == 2:
                # NOTE: Support for only basic authentication
                if auth[0].lower() == 'basic':
                    data = b64decode(auth[1].encode('utf8'))
                    username, password = data.decode('utf8').split(':')
                    if self.authenticate(username, password):
                        return super(BasicAuthMixin, self).dispatch(
                            request, *args, **kwargs
                        )
        text = 'Basic realm="{0!s}"'.format(self.get_realm())
        template = self.get_error_template_name()
        if template:
            response = render(
                request,
                template,
                context=self.get_error_context(request)
            )
        else:
            response = HttpResponse()
        response.status_code = 401
        response['WWW-Authenticate'] = text
        return response


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
        context['cookies'] = OrderedDict(sorted(self.request.COOKIES.items()))
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
        expires = get_expires(self.request.session)
        return {
            'current': expires,
            'expires': datetime.now() + timedelta(minutes=2),
        }

    def get_context_data(self, **kwargs):
        context = super(CacheExpiresView, self).get_context_data(**kwargs)
        context.update(self.get_initial())
        return context


class CacheExpiresImageView(View):
    font = ImageFont.truetype('/usr/share/fonts/dejavu/DejaVuSans.ttf', 25)
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
            if '"{etag}"'.format(etag=etag) == request.META.get('HTTP_IF_NONE_MATCH', None):
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


class SessionView(TemplateView):
    template_name = 'web/session.html'

    def get_context_data(self, **kwargs):
        context = super(SessionView, self).get_context_data(**kwargs)
        context['session'] = OrderedDict(sorted(self.request.session.items()))
        return context


class Http2View(TemplateView):
    template_name = 'web/http2.html'

    def get_context_data(self, **kwargs):
        context = super(Http2View, self).get_context_data(**kwargs)
        context['http2'] = self.request.META['SERVER_PROTOCOL'] == 'HTTP/2.0'
        return context


class FormDataView(CsrfExemptMixin, TemplateView):
    template_name = 'web/form-data.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(FormDataView, self).get_context_data(**kwargs)
        return context


class OrderView(CsrfExemptMixin, FormView):
    template_name = 'web/order.html'
    form_class = forms.OrderForm

    def get_success_url(self):
        return '?pkz={}'.format(self.request.GET.get('pkz'))

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        pkz = self.request.GET.get('pkz')
        if pkz:
            context['pkz'] = pkz
            try:
                context['order'] = models.Order.objects.get(student__pk=pkz)
            except models.Order.DoesNotExist:
                pass
        return context

    def get_form_kwargs(self):
        kwargs = super(OrderView, self).get_form_kwargs()
        pkz = self.request.GET.get('pkz')
        if pkz:
            try:
                kwargs['instance'] = models.Order.objects.get(student__pk=pkz)
            except:
                pass
        return kwargs

    def form_valid(self, form):
        pkz = self.request.GET.get('pkz')
        if pkz:
            order = form.save(commit=False)
            order.student = get_object_or_404(base_models.Student, pk=pkz)
            order.save()
        return super(OrderView, self).form_valid(form)


class AuthView(TemplateView):
    template_name = 'web/auth.html'

    def dispatch(self, request, *args, **kwargs):
        if 'web:auth/password' not in request.session:
            password = ''.join(SystemRandom().choice(digits) for _ in range(4))
            request.session['web:auth/password'] = password
        return super(AuthView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AuthView, self).get_context_data(**kwargs)
        context['password'] = self.request.session.get('web:auth/password')
        return context


class AuthSecureView(BasicAuthMixin, TemplateView):
    template_name = 'web/auth-secure.html'
    error_template_name = 'web/auth-error.html'

    def authenticate(self, username, password):
        session_password = self.request.session.get('web:auth/password')
        return username == 'user' and password == session_password

    def get_error_context(self, request):
        return {
            'password': request.session.get('web:auth/password'),
        }

    def dispatch(self, request, *args, **kwargs):
        if 'web:auth/password' not in request.session:
            return redirect('web:auth')
        return super(AuthSecureView, self).dispatch(request, *args, **kwargs)


class MimeView(TemplateView):
    template_name = 'web/mime.html'

    def dispatch(self, request, *args, **kwargs):
        response = super(MimeView, self).dispatch(request, *args, **kwargs)
        mimetype = kwargs.get('type', None)
        if mimetype:
            response['Content-Type'] = mimetype
        return response
