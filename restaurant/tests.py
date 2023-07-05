from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuTest(TestCase):

	def test_get_menu_item(self):
		item = Menu.objects.create(title='Icecream', price=10, inventory=100)
		self.assertEqual(item, "Icecream : 10")