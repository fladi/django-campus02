#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class Student(models.Model):
    pkz = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return '{self.last_name} {self.first_name} ({self.pkz})'.format(self=self)
