from __future__ import unicode_literals
from django.db import models

from award.models import AwardCategory

class Course(models.Model):
    
    award_category = models.ForeignKey('award.AwardCategory')
