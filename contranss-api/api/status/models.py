__author__ = 'theofilis'

from django.db import models


class StatusType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")

    def __unicode__(self):
        return u"%s" % self.name