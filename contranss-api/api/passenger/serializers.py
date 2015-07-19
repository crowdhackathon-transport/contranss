__author__ = 'theofilis'

from rest_framework import serializers

from models import Passenger


class PassengerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Passenger


class PassengerInfoSerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Passenger