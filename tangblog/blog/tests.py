import datetime

from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.utils import timezone

# Create your tests here.

class BlogPostTest(TestCase):

    def test_create_unpublished(self):
        post = Post(title="Title Me", body=" ")
        post.save()
        self.assertEqual(Post.objects.all().count(), 1)
        post.publish_on  = timezone.now() + datetime.timedelta(days=7)
        post.save();
        self.assertEqual(Post.objects.published().count(), 0)
        post.publish_on = timezone.now()
        post.save()
        self.assertEqual(Post.objects.published().count(), 1)

class BlogViewTests(TestCase):
    def test_feed_url(self):
        response = self.client.get('/feed/')
        self.assertIn('xml', response['Content-Type'])

