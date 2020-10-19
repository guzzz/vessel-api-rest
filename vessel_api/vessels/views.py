from rest_framework import viewsets, mixins

from .models import Vessel
from .serializers import VesselSerializer
from .services import *


class VesselModelViewSet(mixins.CreateModelMixin, 
				   mixins.RetrieveModelMixin, 
				   mixins.DestroyModelMixin,
				   mixins.ListModelMixin,
				   viewsets.GenericViewSet):
	queryset = Vessel.objects.none()
	serializer_class = VesselSerializer

	def get_queryset(self):
		return Vessel.objects.all()

