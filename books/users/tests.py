from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user (
            username='billy',
            email='bill.gates@microsoft.com',
            password='iruletheworld'
        )
        self.assertEqual(user.username, 'billy')
        self.assertEqual(user.email,'bill.gates@microsoft.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser (
            username='billy',
            email='bill.gates@microsoft.com',
            password='iruletheworld'
        )
        self.assertEqual(user.username, 'billy')
        self.assertEqual(user.email,'bill.gates@microsoft.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
