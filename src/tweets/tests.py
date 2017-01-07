from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
# Create your tests here.

from .models import Tweet

User = get_user_model()


class TweetModelTestCase(TestCase):
    def setUp(self):
        some_random_user = User.objects.create(username='maksalizm')

    def test_twwet_item(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            content='Some random content'
        )
        self.assertTrue(obj.content == "Some random content")
        absolute_url = reverse("tweet:detail", kwargs={"pk": 1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)