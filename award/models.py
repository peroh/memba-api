# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
    

class AwardCategory(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    
class Award(models.Model):
    award_category = models.ForeignKey('award.AwardCategory')
    member = models.ForeignKey('member.Member')
    attained = models.DateField()
    
    def __str__(self):
        return self.award_category.__str__()
    
