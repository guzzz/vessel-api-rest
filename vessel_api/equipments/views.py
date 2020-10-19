from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from vessel_api.vessels.models import Vessel

from .models import Equipment
from .serializers import EquipmentSerializer, InactiveEquipmentSerializer
from .services import *


class EquipmentModelViewSet(mixins.CreateModelMixin, 
				   mixins.DestroyModelMixin,
				   mixins.ListModelMixin,
				   viewsets.GenericViewSet):
	queryset = Equipment.objects.all()
	serializer_class = EquipmentSerializer

	def get_queryset(self):
		return Equipment.objects.filter(vessel=self._get_vessel())

	def perform_create(self, serializer):
		serializer.validated_data['vessel'] = self._get_vessel()
		serializer.save()

	def _get_vessel(self):
		vessel_pk = self.kwargs.get('vessel_pk')
		if vessel_pk:
			return get_object_or_404(Vessel, pk=vessel_pk)


	@action(methods=['get'], detail=False)
	def active_equipments(self, request, vessel_pk):
		all_equipments = self.get_queryset()
		active_equipments = all_equipments.filter(status='active')
		serializer = self.serializer_class(active_equipments, many=True)
		return Response(status=status.HTTP_200_OK, data=serializer.data)


class InactivateEquipmentViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
	queryset = Equipment.objects.none()
	serializer_class = InactiveEquipmentSerializer

	def create(self, request, *args, **kwargs):
		list_request = isinstance(request.data, list)
		if list_request:
			serializer = self.get_serializer(data=request.data, many=True)
		else:
			serializer = self.get_serializer(data=request.data, many=False)
		
		if serializer.is_valid():
			equipments = serializer.validated_data
			if inactivate_equipments(equipments):
				response_data = { "success": "Equipment(s) inactivated!" }
				response_status = status.HTTP_200_OK
			else:
				response_data = { "fail": "No equipments were inactivated." }
				response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
			return Response(data=response_data ,status=response_status)
		else:
			return Response(data={ "error(s)": clean_errors(serializer.errors, list_request) }, status=status.HTTP_400_BAD_REQUEST)


