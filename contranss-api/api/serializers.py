__author__ = 'theofilis'

from rest_framework import serializers

from django.contrib.auth import models as model


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = model.User
        fields = ('id', 'url', 'username', 'password', 'email', 'first_name', 'last_name',
                  'is_staff', 'is_active',
                  'password', 'is_superuser', 'driver', 'passenger')


class UserInfoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = model.User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name',
                  'is_staff', 'is_active',
                  'password', 'is_superuser')