__author__ = 'theofilis'

from rest_framework import serializers

from models import Route, Stop, Agency, Service, Trip, TripStop, ServiceDate


class TripSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Trip


class TripStopSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    direction = serializers.BooleanField()

    class Meta:
        model = TripStop


class StopSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Stop


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Route


class AgencySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Agency


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    monday = serializers.BooleanField()
    tuesday = serializers.BooleanField()
    wednesday = serializers.BooleanField()
    thursday = serializers.BooleanField()
    friday = serializers.BooleanField()
    saturday = serializers.BooleanField()
    sunday = serializers.BooleanField()

    class Meta:
        model = Service


class ServiceDateSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = ServiceDate


class RouteInfoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Route


class StopSerializerInfo(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Stop


class AgencySerializerInfo(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Agency


class ServiceSerializerInfo(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    monday = serializers.BooleanField()
    tuesday = serializers.BooleanField()
    wednesday = serializers.BooleanField()
    thursday = serializers.BooleanField()
    friday = serializers.BooleanField()
    saturday = serializers.BooleanField()
    sunday = serializers.BooleanField()

    class Meta:
        model = Service


class ServiceDateSerializerInfo(serializers.ModelSerializer):
    exception_type = serializers.IntegerField()

    class Meta:
        model = ServiceDate


class TripSerializerInfo(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    direction = serializers.BooleanField()
    short_name = serializers.CharField(source='route.short_name')

    class Meta:
        model = Trip
        exclude = ('route', )


class TripStopSerializerInfo(serializers.ModelSerializer):
    stop = StopSerializerInfo()

    class Meta:
        model = TripStop
        exclude = ('id', 'trip', )


class TripStopOnStopSerializerInfo(serializers.ModelSerializer):
    trip = TripSerializerInfo()

    class Meta:
        model = TripStop
        exclude = ('id', 'stop', 'stop_sequence', )