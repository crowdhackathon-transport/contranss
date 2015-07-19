__author__ = 'theofilis'

from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .models import Badge
from .serializers import BadgeSerializer


class DriverLeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response("{}", status=status.HTTP_200_OK)

    def create(self, request):
        return Response("{}", status=status.HTTP_501_NOT_IMPLEMENTED)

    def retrieve(self, request, pk=None):
        return Response("{}", status=status.HTTP_501_NOT_IMPLEMENTED)

    def update(self, request, pk=None):
        return Response("{}", status=status.HTTP_501_NOT_IMPLEMENTED)

    def destroy(self, request, pk=None):
        return Response("{}", status=status.HTTP_501_NOT_IMPLEMENTED)


class PassengerLeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response("{}", status=status.HTTP_200_OK)

    def create(self, request):
        return Response("{}", status=status.HTTP_501_NOT_IMPLEMENTED)

    def retrieve(self, request, pk=None):
        return Response("{}", status=status.HTTP_501_NOT_IMPLEMENTED)

    def update(self, request, pk=None):
        return Response("{}", status=status.HTTP_501_NOT_IMPLEMENTED)

    def destroy(self, request, pk=None):
        return Response("{}", status=status.HTTP_501_NOT_IMPLEMENTED)


class BadgesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser, )
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer