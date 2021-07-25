from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """ Test creating a new user with email """
        email = 'test@test.com'
        password= 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    
    def test_newuser_email(self):

        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email,email.lower())
    
    def test_newuser_invalid(self):
        """User must pass email"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    
    def test_superuser_created(self):
        """test creating new superuser"""

        user = get_user_model().objects.create_superuser('test@test.com','test123@')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)