# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Member(models.Model):
    user = models.ForeignKey('customuser.CustomUser')
    dob = models.DateField()
    nickname = models.CharField(max_length=20)
