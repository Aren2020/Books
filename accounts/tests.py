from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'lolo',
            email = 'lolo@email.com',
            password = 'lolo2000'     
        )
        self.assertEqual(user.username, 'lolo')
        self.assertEqual(user.email, 'lolo@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = 'superlolo',
            email = 'superlolo@email.com',
            password = 'lolo2000'
        )
        self.assertEqual(admin_user.username, 'superlolo')
        self.assertEqual(admin_user.email, 'superlolo@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)