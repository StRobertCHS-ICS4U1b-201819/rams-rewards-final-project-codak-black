# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class History(models.Model):
    name = models.CharField(max_length=120)
    points = models.CharField(max_length=120, null = True, blank = True)
    category = models.CharField(max_length=120, null = True, blank = True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)

# Create your models here.
