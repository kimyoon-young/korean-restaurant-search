# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class Restaurants(models.Model):
    title = models.TextField()
    cate1 = models.TextField()
    cate2 = models.TextField()
    cate3 = models.TextField()
    local = models.TextField()
    city = models.TextField()
    details = models.TextField()

    def __str__(self):
        return self.name

