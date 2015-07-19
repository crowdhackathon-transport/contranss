__author__ = 'theofilis'

from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets

from serializers import UserInfoSerializer, model


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser, )
    queryset = model.User.objects.all()
    serializer_class = UserInfoSerializer
