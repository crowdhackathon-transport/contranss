__author__ = 'theofilis'

from django.db import models

from django.contrib.auth.models import User

from ..gamification.models import Badge


class Driver(models.Model):
    user = models.OneToOneField(User)
    points = models.IntegerField(default=0)
    badges = models.ManyToManyField(Badge)

    def __unicode__(self):
        return u"%s %s" % (self.user.first_name, self.user.last_name)
