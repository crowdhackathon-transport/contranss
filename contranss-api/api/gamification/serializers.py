__author__ = 'theofilis'

from rest_framework import serializers

from models import Badge

class BadgeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Badge