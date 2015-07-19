__author__ = 'theofilis'

from django.db import models


class Advertisment(models.Model):
	id = models.CharField(max_length=255, primary_key=True)

	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

	ad_slug = models.CharField(max_length=255)
	ad_description = models.TextField(default="")
	ad_image_src = models.URLField()
	ad_href = models.URLField()
	ad_type = models.CharField(max_length=255)

	budget = models.FloatField()
	current_cost = models.FloatField()

	def is_enabled(self):
		return False

	def is_on_budget(self):
		return current_cost <= budget