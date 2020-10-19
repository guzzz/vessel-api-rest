from django.test import TestCase
from django.test import Client

from vessel_api.vessels.models import Vessel
from .models import Equipment


class EquipmentTest(TestCase):
	@classmethod
	def setUpClass(cls):
		super(EquipmentTest, cls).setUpClass()
		print('======================================================================')
		print('==> INITIALIZING Equipments Tests...')
		print('======================================================================')
		print('... CREATING initial Equipment ..............................')
		vessel_instance = Vessel.objects.create(code="MV1")
		Equipment.objects.create(code="EQ1", name="Equipment 1", location="X", vessel=vessel_instance)
		Equipment.objects.create(code="EQ2", name="Equipment 2", location="Y", vessel=vessel_instance)
		print('----------------------------------------------------------------------')

	def setup():
		self.client = Client()

	def test_list_equipments(self):
		print('==> LIST: [GET] /vessels/MV1/equipments/')
		response = self.client.get('/vessels/MV1/equipments/')
		self.assertEqual(response.status_code, 200)
		print('----------------------------------------------------------------------')

	def test_post_equipment(self):
		print('==> CREATE: [POST] /vessels/MV1/equipments/')
		response = self.client.post('/vessels/MV1/equipments/', {'code': 'EQ3', 'name': 'Equipment 3', 'location': 'Z'})
		self.assertEqual(response.status_code, 201)
		self.assertEqual(response.json(), {'code': 'EQ3', 'name': 'Equipment 3', 'location': 'Z', 'status': 'active'})
		print('----------------------------------------------------------------------')

	def test_list_active_equipments(self):
		print('==> LIST: [GET] /vessels/MV1/equipments/active_equipments/')
		response = self.client.get('/vessels/MV1/equipments/active_equipments/')
		self.assertEqual(response.status_code, 200)
		print('----------------------------------------------------------------------')

	def test_delete_equipment(self):
		print('==> DESTROY: [DELETE] /vessels/MV1/equipments/EQ2/')
		response = self.client.delete('/vessels/MV1/equipments/EQ2/')
		self.assertEqual(response.status_code, 204)
		print('----------------------------------------------------------------------')

	def test_inactivate_equipment(self):
		print('==> CUSTOM: [POST] /inactivate-equipments/')
		response = self.client.post('/inactivate-equipments/', {'code': 'EQ1'})
		key_info = response.json().popitem()[0]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(key_info, 'success')
		print('----------------------------------------------------------------------')

	def test_inactivate_equipments(self):
		print('==> CUSTOM: [POST] /inactivate-equipments/')
		data = [{'code': 'EQ1'},{'code': 'EQ2'}]
		response = self.client.post('/inactivate-equipments/',data=data, content_type='application/json')
		key_info = response.json().popitem()[0]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(key_info, 'success')
		print('----------------------------------------------------------------------')

