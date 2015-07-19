__author__ = 'theofilis'

from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .serializers import PassengerInfoSerializer
from .models import Passenger

import uuid

from elasticsearch import Elasticsearch
es = Elasticsearch()


def prepare(res):
    res = res['hits']
    del res['max_score']
    res['size'] = res['total']
    del res['total']
    return res


class PassengerViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAdminUser, )
    queryset = Passenger.objects.all()
    serializer_class = PassengerInfoSerializer

    @detail_route(methods=['get', 'post', 'delete'])
    def status(self, request, pk=None):
        if request.method == 'GET':
            query = {
                "query": {
                    "bool": {
                        "must": [{
                                "match": {
                                    "user.id": pk
                                }
                        }]
                    }
                },
                "sort": [{
                    "timestamp" : "desc"
                }]
            }

            res = es.search(index="posts", body=query)
            return Response(prepare(res), status=status.HTTP_200_OK)

        if request.method == 'POST':
            document = request.data
            doc_id = uuid.uuid4()

            res = es.index(index="posts", doc_type="post", id=doc_id, body=document)
            return Response(res, status=status.HTTP_501_NOT_IMPLEMENTED)      

    @detail_route(methods=['get', 'post', 'delete'])
    def favourites(self, request, pk=None):
        return Response("", status=status.HTTP_501_NOT_IMPLEMENTED)
