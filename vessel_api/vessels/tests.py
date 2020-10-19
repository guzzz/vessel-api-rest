from django.test import TestCase
from django.test import Client

from .models import Vessel


class VesselTest(TestCase):
	@classmethod
	def setUpClass(cls):
		super(VesselTest, cls).setUpClass()
		print('======================================================================')
		print('==> INITIALIZING Vessels Tests...')
		print('======================================================================')
		print('... CREATING initial Vessel ..............................')
		Vessel.objects.create(code="MV100")
		Vessel.objects.create(code="MV101")
		print('----------------------------------------------------------------------')

	def setup():
		self.client = Client()

	def test_list_vessels(self):
		print('==> LIST: [GET] /vessels')
		response = self.client.get('/vessels/')
		self.assertEqual(response.status_code, 200)
		print('----------------------------------------------------------------------')

	def test_retrieve_vessel(self):
		print('==> RETRIEVE: [GET] /vessels/')
		response = self.client.get('/vessels/MV100/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json(), {'code': 'MV100'})
		print('----------------------------------------------------------------------')

	def test_post_vessel(self):
		print('==> CREATE: [POST] /vessels/')
		response = self.client.post('/vessels/', {'code': 'MV102'})
		self.assertEqual(response.status_code, 201)
		self.assertEqual(response.json(), {'code': 'MV102'})
		print('----------------------------------------------------------------------')

	def test_delete_vessel(self):
		print('==> DESTROY: [DELETE] /vessels/')
		response = self.client.delete('/vessels/MV101/')
		self.assertEqual(response.status_code, 204)
		print('----------------------------------------------------------------------')



