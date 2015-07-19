# -*- coding: utf-8 -*-

__author__ = 'theofilis'

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from models import Route, Stop, Agency, Service, Trip, TripStop, ServiceDate


class AgencyResource(resources.ModelResource):
    class Meta:
        model = Agency
        fields = ('id', 'name', 'url', 'timezone', 'lang', 'phone')


class TripResource(resources.ModelResource):
    class Meta:
        model = Trip
        fields = ('route', 'service', 'id', 'head_sign', 'direction', 'block', 'shape')


class RouteResource(resources.ModelResource):
    class Meta:
        model = Route


class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service


class ServiceDateResource(resources.ModelResource):
    class Meta:
        model = ServiceDate


class StopResource(resources.ModelResource):
    class Meta:
        model = Stop
        fields = ('id', 'code', 'name', 'desc', 'lat', 'lon', 'location_type')


class TripStopResource(resources.ModelResource):
    class Meta:
        model = TripStop
        fields = ('trip', 'stop', 'stop_sequence', 'pickup_type', 'drop_off_type')

@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    resource_class = ServiceResource
    list_display = ('id', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'start_date', 'end_date')


@admin.register(TripStop)
class TripStopAdmin(ImportExportModelAdmin):
    resource_class = TripStopResource
    list_display = ('trip', 'stop', 'stop_sequence', 'pickup_type', 'drop_off_type')


@admin.register(ServiceDate)
class ServiceDateAdmin(ImportExportModelAdmin):
    resource_class = ServiceDateResource
    list_display = ('service', 'date', 'exception_type', )


@admin.register(Trip)
class TripAdmin(ImportExportModelAdmin):
    resource_class = TripResource
    list_display = ('id', 'route', 'service')


@admin.register(Agency)
class AgencyAdmin(ImportExportModelAdmin):
    resource_class = AgencyResource
    list_display = ('name', 'url', 'timezone', 'lang', 'phone')
    search_fields = ['name']


@admin.register(Stop)
class StopAdmin(ImportExportModelAdmin):
    resource_class = StopResource
    search_fields = ['name']
    list_display = ('code', 'name', 'desc')


def get_type(obj):
    if obj.type == 0:
        return u"ΤΡΟΛΕΙ"
    elif obj.type == 1:
        return u"ΜΕΤΡΟ"
    elif obj.type == 2:
        return u"ΤΡΑΜ"
    elif obj.type == 3: 
        return u"ΛΕΩΦΟΡΕΙΟ"


@admin.register(Route)
class RouteAdmin(ImportExportModelAdmin):
    resource_class = RouteResource
    search_fields = ['short_name']
    list_display = ('short_name', 'long_name', get_type)
    list_filter = ('type', )
