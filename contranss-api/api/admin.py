__author__ = 'theofilis'

from import_export import resources

from django.contrib.auth import models as model


class UserResource(resources.ModelResource):

    class Meta:
        model = model.User