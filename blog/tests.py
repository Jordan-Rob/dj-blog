from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

# Create your tests here.


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='TestUser',
            email=' test@mail.co',
            password='secret'

        )

        self.post = Post.objects.create(
            title='A good title',
            body='nice body content',
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title='a simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{ self.post.body }', 'nice body content')
        self.assertEqual(f'{self.post.author}', 'Testuser')
