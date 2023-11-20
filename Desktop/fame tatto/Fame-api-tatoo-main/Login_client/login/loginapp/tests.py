from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'devesh',
            'email': 'devesh@weboappdiscovery.com',
            'password': 'weboappdiscovery'
        }

    def test_user_registration(self):
        response = self.client.post('/api/register/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    # Add more test cases for login, authentication, etc.


