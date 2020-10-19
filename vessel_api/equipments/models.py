from django.db import models

from .choices import ACTIVATION_CHOICES


class Equipment(models.Model):
	code = models.CharField(primary_key=True, max_length=50)
	name = models.CharField(max_length=255, blank=False)
	location = models.CharField(max_length=255, blank=False)
	status = models.CharField(blank=True, default='active', max_length=10, choices=ACTIVATION_CHOICES)
	vessel = models.ForeignKey(
		to='vessels.Vessel',
		related_name='%(class)s',
		on_delete=models.CASCADE
	)
