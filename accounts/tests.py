from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserSignupTest(TestCase):

    def test_create_user(self):
        new_user = User.objects.create_user(username='john', password='glass onion')
        user = User.objects.filter(username="john")
        self.assertIn(new_user, user)

    def test_user_signup(self):
        resp = self.client.post(reverse('signup'), {'username': 'john', 'password': 'glass onion'})
        self.assertEqual(resp.status_code, 200)

    def test_home_page(self):
        resp = self.client.get(reverse('dashboard:dashboard'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/accounts/login/?next=/')

    def test_login_user(self):
        User.objects.create_user(username='john', password='glass onion')
        resp = self.client.post(reverse('login'), {'username': 'john', 'password': 'glass onion'})
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/')
