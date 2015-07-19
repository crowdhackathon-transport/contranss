__author__ = 'theofilis'

from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, status, filters
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from elasticsearch import Elasticsearch

from .serializers import RouteInfoSerializer, StopSerializerInfo, AgencySerializerInfo, ServiceDateSerializerInfo, ServiceSerializerInfo, \
    TripSerializerInfo, TripStopSerializerInfo, TripStopOnStopSerializerInfo
from models import Route, Stop, Agency, Service, Trip, ServiceDate


class ServiceDateViewSet(viewsets.ModelViewSet):
#    permission_classes = (IsAdminUser, )
    queryset = ServiceDate.objects.all()
    serializer_class = ServiceDateSerializerInfo


class AgencyViewSet(viewsets.ModelViewSet):
#    permission_classes = (IsAdminUser, )
    queryset = Agency.objects.all()
    serializer_class = AgencySerializerInfo


class ServiceViewSet(viewsets.ModelViewSet):
#    permission_classes = (IsAdminUser, )
    queryset = Service.objects.all()
    serializer_class = ServiceSerializerInfo


class RouteViewSet(viewsets.ModelViewSet):
#    permission_classes = (IsAdminUser, )
    queryset = Route.objects.all()
    serializer_class = RouteInfoSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('type', )
    search_fields = ('short_name', 'long_name')
    ordering_fields = ('short_name', 'long_name', 'type')

    @detail_route(methods=['get', 'post', 'delete'])
    def trips(self, request, pk=None):
        obj = self.get_object()

        trips = []
        ids = []
        for trip in obj.trips.all():
            if trip.service.id not in ids:
                trips.append(trip)
                ids.append(trip.service.id)

        serializer = TripSerializerInfo(trips, many=True, context={'request': request})
        return Response(serializer.data)


class TripViewSet(viewsets.ModelViewSet):
#    permission_classes = (IsAdminUser, )
    queryset = Trip.objects.all()
    serializer_class = TripSerializerInfo

    @detail_route(methods=['get', 'post', 'delete'])
    def stops(self, request, pk=None):
        obj = self.get_object()
        serializer = TripStopSerializerInfo(obj.stops, many=True, context={'request': request})
        return Response(serializer.data)


class StopViewSet(viewsets.ModelViewSet):
#    permission_classes = (IsAdminUser, )
    queryset = Stop.objects.all()
    serializer_class = StopSerializerInfo

    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('location_type', )
    search_fields = ('name', )
    ordering_fields = ('name', 'location_type')

    @detail_route(methods=['get', 'post', 'delete'])
    def routes(self, request, pk=None):
        obj = self.get_object()

        trips = []
        ids = []
        for trip in obj.trips.all():
            if trip.trip.route.short_name not in ids:
                trips.append(trip)
                ids.append(trip.trip.route.short_name)

        serializer = TripStopOnStopSerializerInfo(trips, many=True, context={'request': request})
        return Response(serializer.data)

    @detail_route(methods=['get', 'post', 'delete'])
    def status(self, request, pk=None):
        return Response("", status=status.HTTP_501_NOT_IMPLEMENTED)

    @detail_route(methods=['get', 'post'])
    def track(self, request, pk=None):
        return Response("", status=status.HTTP_501_NOT_IMPLEMENTED)


es = Elasticsearch()

def prepare(res):
    res = res['hits']
    del res['max_score']
    res['size'] = res['total']
    del res['total']
    return res

class StopNearViewSet(viewsets.ViewSet):
    def list(self, request):
        lat = request.query_params.get('lat', 0)
        lon = request.query_params.get('lon', 0)
        distance = request.query_params.get('distance', "0.2km")

        query = {
            "query": {
                "filtered": {
                  "filter": {
                    "geo_distance": {
                      "distance": distance, 
                      "location": { 
                        "lat":  lat,
                        "lon": lon
                      }
                    }
                  }
                }
            },
            "sort": [
            {
              "_geo_distance": {
                "location": { 
                  "lat":  lat,
                  "lon": lon
                },
                "order":         "asc",
                "unit":          "m", 
                "distance_type": "plane" 
              }
            }
          ]
        }

        res = es.search(index="stop", body=query)
        return Response(prepare(res), status=status.HTTP_200_OK)

    def create(self, request):
        return Response("")

    def retrieve(self, request, pk=None):
        return Response("")

    def update(self, request, pk=None):
        return Response("")

    def destroy(self, request, pk=None):
        return Response("")