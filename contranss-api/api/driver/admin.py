__author__ = 'theofilis'

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from models import Driver


class DriverResource(resources.ModelResource):
    class Meta:
        model = Driver


@admin.register(Driver)
class DriverAdmin(ImportExportModelAdmin):
    resource_class = DriverResource
