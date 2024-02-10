
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User


class ArticleAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client = APIClient()

    def test_create_article(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/articles/', {'title': 'Test Article', 'content': 'Test content'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_article_with_invalid_data(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/articles/', {'title': 'Short', 'content': 'Test content'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)