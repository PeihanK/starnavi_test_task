from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from posts.models import Post
import json


class PostCreateTestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        # Create new post
        url = '/api/posts/'
        data = {
            'title': 'Test Post',
            'content': 'This is a test post content'
        }
        response = self.client.post(url, data, format='json')

        # Check if Status 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if new post is in DB
        post = Post.objects.get(id=response.data['id'])
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'This is a test post content')

    def test_create_toxic_post(self):
        url = '/api/posts/'
        data = {
            'title': 'Offensive Post',
            'content': 'This post contains offensive word: damn'
        }
        response = self.client.post(url, data, format='json')

        # Check if Status 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertIn('is_blocked', response.data)
        self.assertTrue(response.data['is_blocked'])

        # Check if field is_blocked=True
        post = Post.objects.get(id=response.data['id'])
        self.assertTrue(post.is_blocked)

    def test_create_post_without_authentication(self):
        self.client.logout()
        url = '/api/posts/'
        data = {
            'title': 'Unauthenticated Post',
            'content': 'This is a post without authentication'
        }
        response = self.client.post(url, data, format='json')

        # Check if Status 401 (Unauthorized)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
