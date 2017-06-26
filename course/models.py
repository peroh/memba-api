from __future__ import unicode_literals
from django.db import models

from award.models import AwardCategory

class Course(models.Model):
    title = models.CharField(max_length=128)
    award_category = models.ForeignKey('award.AwardCategory')
    attendees = models.ManyToManyField('member.Member', blank=True)
    
    