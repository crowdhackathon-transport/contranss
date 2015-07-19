__author__ = 'theofilis'

from django.db import models

from django.contrib.auth.models import User

from ..gamification.models import Badge
import math


class Passenger(models.Model):
    user = models.OneToOneField(User)
    points = models.IntegerField(default=0)
    badges = models.ManyToManyField(Badge)

    def level(self):
    	return int(math.floor((1+math.sqrt(self.points/125 + 1))/2))

    def __unicode__(self):
        return u"%s %s" % (self.user.first_name, self.user.last_name)
