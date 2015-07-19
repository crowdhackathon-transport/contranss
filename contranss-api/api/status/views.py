__author__ = 'theofilis'

from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from elasticsearch import Elasticsearch

from .serializers import StatusTypeSerializer
from .models import StatusType

from ..route.models import Route
from ..route.serializers import RouteInfoSerializer

import uuid

es = Elasticsearch()

def prepare(res):
    res = res['hits']
    del res['max_score']
    res['size'] = res['total']
    del res['total']
    return res

class StatusTypeDateViewSet(viewsets.ModelViewSet):
#    permission_classes = (IsAdminUser, )
    queryset = StatusType.objects.all()
    serializer_class = StatusTypeSerializer


class StatusViewSet(viewsets.ViewSet):

    def list(self, request):
        document = request.query_params
        page = int(request.query_params.get('page', 0))
        size = int(request.query_params.get('size', 10))
        route = request.query_params.get('route', '*')

        start = page * size
        query = {
            "from": start,
            "size": size,
            "query": {
                "query_string": {
              "query": "route.id:" + route,
              "analyze_wildcard": "true"
            }
            },
            "sort": [{
                "timestamp" : "desc"
            }]
        }

        res = es.search(index="posts", body=query)
        return Response(prepare(res), status=status.HTTP_200_OK)

    def create(self, request):
        document = request.data
        doc_id = uuid.uuid4()

        document['type'] = StatusTypeSerializer(StatusType.objects.get(pk=document['type'])).data
        document['route'] = RouteInfoSerializer(Route.objects.get(pk=document['route'])).data

        res = es.index(index="posts", doc_type="post", id=doc_id, body=document)
        return Response(res, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        res = es.get(index="posts", doc_type='post', id=pk)
        return Response(res, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        document = request.data
        res = es.index(index="posts", doc_type="post", id=pk, body=document)
        return Response(res, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        res = es.delete(index="posts", doc_type='post', id=pk)
        return Response(res, status=status.HTTP_200_OK)


class StatusRouteViewSet(viewsets.ViewSet):

    def list(self, request):
        document = request.query_params
        page = int(request.query_params.get('page', 0))
        size = int(request.query_params.get('size', 10))
        route = int(request.query_params.get('route', ''))

        start = page * size
        query = {
            "from": start,
            "size": size,
            "query": {
            "query_string": {
              "query": "route.id:" + route,
              "analyze_wildcard": true
            }
          },
            "sort": [{
                "timestamp" : "desc"
            }]
        }

        res = es.search(index="posts", body=query)
        return Response(prepare(res), status=status.HTTP_200_OK)

    def create(self, request):
        document = request.data
        doc_id = uuid.uuid4()

        document['type'] = StatusTypeSerializer(StatusType.objects.get(pk=document['type'])).data
        document['route'] = RouteInfoSerializer(Route.objects.get(pk=document['route'])).data

        res = es.index(index="posts", doc_type="post", id=doc_id, body=document)
        return Response(res, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        res = es.get(index="posts", doc_type='post', id=pk)
        return Response(res, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        document = request.data
        res = es.index(index="posts", doc_type="post", id=pk, body=document)
        return Response(res, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        res = es.delete(index="posts", doc_type='post', id=pk)
        return Response(res, status=status.HTTP_200_OK)