import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatube_api.settings')

from django.test import TestCase
from django.contrib.auth import get_user_model
from posts.models import Post, Group, Comment, Follow

User = get_user_model()


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser')
        self.group = Group.objects.create(title='Test Group', slug='test-group')
        self.post = Post.objects.create(
            text='Test post content',
            author=self.user,
            group=self.group
        )

    def test_post_creation(self):
        self.assertEqual(self.post.text, 'Test post content')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.group.title, 'Test Group')

    def test_post_str_method(self):
        self.assertIsInstance(str(self.post), str)

    def test_group_creation(self):
        self.assertEqual(self.group.title, 'Test Group')
        self.assertEqual(self.group.slug, 'test-group')

    def test_group_str_method(self):
        self.assertEqual(str(self.group), self.group.title)

    def test_comment_creation(self):
        comment = Comment.objects.create(
            text='Test comment',
            author=self.user,
            post=self.post
        )
        self.assertEqual(comment.text, 'Test comment')
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.post, self.post)

    def test_follow_creation(self):
        another_user = User.objects.create_user(username='anotheruser')
        follow = Follow.objects.create(
            user=self.user,
            following=another_user
        )
        self.assertEqual(follow.user, self.user)
        self.assertEqual(follow.following, another_user)
