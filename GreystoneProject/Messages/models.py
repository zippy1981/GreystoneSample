# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Message(models.Model):
    message_text = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('id',)