#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.core.urlresolvers import reverse_lazy as reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FormActions

from . import models


class CookieForm(forms.Form):
    key = forms.CharField(label='Key', max_length=100)
    value = forms.CharField(label='Value', widget=forms.Textarea)
    domain = forms.CharField(label='Domain', max_length=255, required=False)
    httponly = forms.BooleanField(label='HTTP-only', required=False)
    secure = forms.BooleanField(label='Secure', required=False)
    expires = forms.DateTimeField(label='Expires', required=False)
    path = forms.CharField(label='Path', max_length=4096, required=False)

    def __init__(self, *args, **kwargs):
        super(CookieForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form-cookie'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('web:cookies')
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'key',
            'value',
            'httponly',
            'secure',
            'domain',
            'path',
            'expires',
            FormActions(
                Submit('save', 'Save cookie'),
            )
        )


class CacheExpiresForm(forms.Form):
    expires = forms.DateTimeField(label='Expires')

    def __init__(self, *args, **kwargs):
        super(CacheExpiresForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form-cache-expires'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('web:cache/expires')
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'expires',
            FormActions(
                Submit('save', 'Save expiration'),
            )
        )


class CacheEtagForm(forms.Form):
    etag = forms.CharField(label='ETag')
    age = forms.IntegerField(label='max-age', min_value=1)

    def __init__(self, *args, **kwargs):
        super(CacheEtagForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form-cache-etag'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('web:cache/etag')
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'etag',
            'age',
            FormActions(
                Submit('save', 'Save settings'),
            )
        )


class CacheControlForm(forms.Form):
    control = forms.CharField(label='Cache-Control')

    def __init__(self, *args, **kwargs):
        super(CacheControlForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form-cache-control'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('web:cache/control')
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'control',
            FormActions(
                Submit('save', 'Save settings'),
            )
        )


class OrderForm(forms.ModelForm):

    class Meta:
        model = models.Order
        exclude = ['student']


class RedirectForm(forms.Form):
    status = forms.ChoiceField(
        label='Status',
        choices=(
            (301, 'Moved Permanently'),
            (302, 'Found (Moved Temporarily)'),
        )
    )
    location = forms.CharField(label='Location')

    def __init__(self, *args, **kwargs):
        super(RedirectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form-redirect'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('web:redirect')
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'status',
            'location',
            FormActions(
                Submit('save', 'Redirect'),
            )
        )


