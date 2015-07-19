__author__ = 'theofilis'

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from models import Passenger


class PassengerResource(resources.ModelResource):
    class Meta:
        model = Passenger


@admin.register(Passenger)
class PassengerAdmin(ImportExportModelAdmin):
    resource_class = PassengerResource
    search_fields = ['first_name']
    list_display = ('user', 'points', 'level')

