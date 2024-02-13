from django.test import TestCase


from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase

class YourApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        url = 'http://localhost:8000/api/auth/signup/'
        data = {
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser@example.com')