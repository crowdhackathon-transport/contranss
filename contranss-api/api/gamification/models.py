__author__ = 'theofilis'

from django.db import models


class Badge(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    badge_type = models.CharField(max_length=255, default="")
    bonus_xp = models.IntegerField(default=0)
   
    def __unicode__(self):
        return u"%s" % self.name