from rest_framework import serializers

from .models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Equipment
		exclude = ('vessel',)


class InactiveEquipmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Equipment
		exclude = ('vessel','name','location','status')
		extra_kwargs = {
			'code': {'validators': []},
		}
		ref_name=None

	def validate_code(self, code):
		if not Equipment.objects.filter(code=code).exists():
			raise serializers.ValidationError({
				code: 'Equipment does not exist.'
			})
		return code
