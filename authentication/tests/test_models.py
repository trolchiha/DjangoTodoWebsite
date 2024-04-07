from django.test import TestCase
from authentication.models import User

class TestModels(TestCase):
    def test_should_create_user(self):
        user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
        )
        user.set_password('password123')
        user.save()

        self.assertEqual(str(user), 'testuser@email.com')

            