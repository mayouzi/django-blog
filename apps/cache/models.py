# coding=utf-8

__author__ = 'mayor'

from caching.base import CachingMixin
from django.db import models

class CacheObject(CachingMixin, models.Model):
     # objects = CachingManager()
     class Meta:
         abstract=True