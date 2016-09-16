#!/usr/bin/python
# -*- coding: utf-8 -*-

import uuid

from pathlib import PurePath

from django.utils.deconstruct import deconstructible


@deconstructible
class RandomFileName(object):

    def __eq__(self, other):
        return True

    def __call__(self, instance, filename):
        path = PurePath(
            instance._meta.app_label,
            instance._meta.model_name,
            str(uuid.uuid4())
        )
        return str(path.with_suffix(PurePath(filename).suffix))
