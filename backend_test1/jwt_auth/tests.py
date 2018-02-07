from django.test import TestCase
from .models import User
# Create your tests here.
class ModelTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username = 'domidog',name = 'domidog')

    def test_model(self):
        username = User.objects.get(id = 1)
        expected_object_name = f'{username.name}'
        self.assertEqual(expected_object_name,'domidog')
