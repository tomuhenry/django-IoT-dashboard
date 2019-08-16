from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from . import views, services


class DashboardTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='john', password='glass onion')
        self.client.post(reverse('login'), {'username': 'john', 'password': 'glass onion'})

    def test_view(self):
        resp = self.client.get(reverse('dashboard:dashboard'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'dashboard/dashboard.html')

    def test_services(self):
        resp = services.get_channel_data()
        self.assertIn('feeds', resp)

