from django.db import models


class Vessel(models.Model):
	code = models.CharField(primary_key=True, max_length=50)

	def __str__(self):
		return self.code
