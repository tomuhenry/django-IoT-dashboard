from django.test import TestCase
from django.contrib.auth.models import User


class UserSignupTest(TestCase):

    def test_user_signup(self):
        new_user = User.objects.create_user(username='john', password='glass onion')
        user = User.objects.filter(username="john")
        self.assertIn(new_user, user)
