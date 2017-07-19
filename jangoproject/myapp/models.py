# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=255)
    age=models.IntegerField(default=0)
    contact=models.IntegerField(max_length=20)
    create_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)


