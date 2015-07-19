__author__ = 'theofilis'

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from models import Badge

class BadgeResource(resources.ModelResource):
    class Meta:
        model = Badge
   
@admin.register(Badge)
class BadgeAdmin(ImportExportModelAdmin):
    resource_class = BadgeResource
    search_fields = ['name']
    list_filter = ('name', )
    fields = ('name', )