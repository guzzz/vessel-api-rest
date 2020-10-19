from .models import Equipment


def inactivate_equipments(equipments):
	equipments_list = []
	if isinstance(equipments, list):
		for item in equipments:
			equipments_list.append(item['code'])
	else:
		equipments_list.append(equipments['code'])
	updated_objects = Equipment.objects.filter(code__in=equipments_list).update(status='inactive')
	if updated_objects:
		return True
	else:
		return False


def clean_errors(serializer_errors, list_request):
	if list_request:
		return list(filter(None, serializer_errors))
	else:
		return serializer_errors