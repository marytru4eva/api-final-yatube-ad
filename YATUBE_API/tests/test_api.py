import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatube_api.settings')

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from posts.models import Post, Group, Comment, Follow

User = get_user_model()


class PostAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.another_user = User.objects.create_user(
            username='anotheruser',
            password='testpass123'
        )
        self.group = Group.objects.create(
            title='Test Group',
            slug='test-group',
            description='Test Description'
        )
        self.post = Post.objects.create(
            text='Test post content',
            author=self.user,
            group=self.group
        )
        self.client.force_authenticate(user=self.user)

    def test_get_posts_list(self):
        response = self.client.get('/api/v1/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_post_authenticated(self):
        data = {'text': 'New post', 'group': self.group.id}
        response = self.client.post('/api/v1/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_create_post_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {'text': 'New post'}
        response = self.client.post('/api/v1/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_single_post(self):
        response = self.client.get(f'/api/v1/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], self.post.text)

    def test_update_post_author(self):
        data = {'text': 'Updated text'}
        response = self.client.patch(f'/api/v1/posts/{self.post.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.text, 'Updated text')

    def test_update_post_not_author(self):
        self.client.force_authenticate(user=self.another_user)
        data = {'text': 'Hacked text'}
        response = self.client.patch(f'/api/v1/posts/{self.post.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_post_author(self):
        response = self.client.delete(f'/api/v1/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

    def test_delete_post_not_author(self):
        self.client.force_authenticate(user=self.another_user)
        response = self.client.delete(f'/api/v1/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class GroupAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.group = Group.objects.create(title='Test Group', slug='test-group', description='Test Description')

    def test_get_groups_list(self):
        response = self.client.get('/api/v1/groups/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_group(self):
        response = self.client.get(f'/api/v1/groups/{self.group.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.group.title)


class CommentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.post = Post.objects.create(text='Test post', author=self.user)
        self.comment = Comment.objects.create(
            text='Test comment',
            author=self.user,
            post=self.post
        )
        self.client.force_authenticate(user=self.user)

    def test_get_comments_list(self):
        response = self.client.get(f'/api/v1/posts/{self.post.id}/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_comment_authenticated(self):
        data = {'text': 'New comment'}
        response = self.client.post(
            f'/api/v1/posts/{self.post.id}/comments/',
            data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    def test_create_comment_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {'text': 'New comment'}
        response = self.client.post(
            f'/api/v1/posts/{self.post.id}/comments/',
            data
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class FollowAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.another_user = User.objects.create_user(
            username='anotheruser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)

    def test_follow_user(self):
        data = {'following': self.another_user.username}
        response = self.client.post('/api/v1/follow/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Follow.objects.count(), 1)

    def test_follow_self_forbidden(self):
        data = {'following': self.user.username}
        response = self.client.post('/api/v1/follow/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_follows_list(self):
        Follow.objects.create(user=self.user, following=self.another_user)
        response = self.client.get('/api/v1/follow/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
