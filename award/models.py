# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
    

class AwardCategory(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    members = models.ManyToManyField('member.Member', through='award.Award')
    
    
class Award(models.Model):
    award_category = models.ForeignKey('award.AwardCategory')
    member = models.ForeignKey('member.Member')
    attained = models.DateField()