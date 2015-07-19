__author__ = 'theofilis'

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from models import StatusType

class StatusTypeResource(resources.ModelResource):
    class Meta:
        model = StatusType
   
@admin.register(StatusType)
class StatusTypeAdmin(ImportExportModelAdmin):
    resource_class = StatusTypeResource
    search_fields = ['name']
    fields = ('name', 'description', )