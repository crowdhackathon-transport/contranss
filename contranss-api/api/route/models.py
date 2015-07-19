__author__ = 'theofilis'

from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    timezone = models.CharField(max_length=32)
    lang = models.CharField(max_length=3)
    phone = models.CharField(max_length=32)
    fare_url = models.URLField()

    def __unicode__(self):
        return u"%s" % self.name


class Stop(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    code = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    desc = models.CharField(max_length=256)
    lat = models.FloatField()
    lon = models.FloatField()
    location_type = models.CharField(max_length=128)

    def __unicode__(self):
        return u"%s %s" % (self.code, self.name)


class Service(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    monday = models.BinaryField()
    tuesday = models.BinaryField()
    wednesday = models.BinaryField()
    thursday = models.BinaryField()
    friday = models.BinaryField()
    saturday = models.BinaryField()
    sunday = models.BinaryField()

    start_date = models.CharField(max_length=8)
    end_date = models.CharField(max_length=8)

    def __unicode__(self):
        return u"%s" % self.id


class ServiceDate(models.Model):
    service = models.ForeignKey(Service)
    date = models.CharField(max_length=8)
    exception_type = models.CharField(max_length=8)

    def __unicode__(self):
        return u"%s" % self.service_id


class Route(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    short_name = models.CharField(max_length=3)
    long_name = models.CharField(max_length=124)
    desc = models.CharField(max_length=512)
    type = models.IntegerField()
    color = models.CharField(max_length=6)
    text_color = models.CharField(max_length=6)

    def __unicode__(self):
        return u"%s %s" % (self.short_name, self.long_name)


class Trip(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    route = models.ForeignKey('Route', related_name='trips')
    service = models.ForeignKey('Service', related_name='trips')
    head_sign = models.CharField(max_length=128)
    direction = models.BinaryField()
    block = models.IntegerField()
    shape = models.CharField(max_length=64)

    def __unicode__(self):
        return u"%s" % self.id


class TripStop(models.Model):
    trip = models.ForeignKey('Trip', related_name='stops')
    stop = models.ForeignKey('Stop', related_name='trips')
    stop_sequence = models.IntegerField()
    pickup_type = models.IntegerField()
    drop_off_type = models.IntegerField()