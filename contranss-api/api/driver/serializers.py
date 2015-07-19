__author__ = 'theofilis'

from rest_framework import serializers

from models import Driver


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Driver


class DriverInfoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Driver