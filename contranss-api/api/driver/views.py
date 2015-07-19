__author__ = 'theofilis'

from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .serializers import DriverInfoSerializer
from .models import Driver

from elasticsearch import Elasticsearch
es = Elasticsearch()


class DriverViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser, )
    queryset = Driver.objects.all()
    serializer_class = DriverInfoSerializer

    @detail_route(methods=['get', 'post'])
    def status(self, request, pk=None):
    	if request.method == 'GET':
    		res = es.search(index="posts", body={"query": {"match_all": {}}})
    		return Response(res, status=status.HTTP_501_NOT_IMPLEMENTED)

    	if request.method == 'POST':
    		return Response("", status=status.HTTP_501_NOT_IMPLEMENTED)        

    @detail_route(methods=['get', 'post'])
    def track(self, request, pk=None):
        return Response("", status=status.HTTP_501_NOT_IMPLEMENTED)