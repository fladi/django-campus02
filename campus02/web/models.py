#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class Order(models.Model):
    student = models.OneToOneField('base.Student')
    first_name = models.CharField(max_length=256, blank=False)
    last_name = models.CharField(max_length=256, blank=False)
    address = models.CharField(max_length=256, blank=False)
    zip_code = models.PositiveSmallIntegerField(blank=False)
    city = models.CharField(max_length=256, blank=False)
    email = models.EmailField(blank=False)
    product = models.CharField(max_length=256, blank=False)
    amount = models.PositiveSmallIntegerField(blank=False)
    delivery = models.CharField(max_length=256, blank=False)
    gift = models.BooleanField(default=False, blank=False)
    image = models.ImageField()
    comment = models.TextField(blank=True)
