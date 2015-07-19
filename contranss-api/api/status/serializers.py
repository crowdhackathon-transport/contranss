__author__ = 'theofilis'

from rest_framework import serializers

from models import StatusType

class StatusTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = StatusType