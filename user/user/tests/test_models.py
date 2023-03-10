"""
Test models in user app.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


def create_user(email='test@example.com',
                password='testpass',
                username='testusername'):
    """Handler function to create user"""
    return get_user_model().objects.create_user(email, password, username)


class ModelsTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successfull(self):
        """Test creating user with email by using default user model."""
        email = 'test@example.com'
        password = 'testpassword'
        username = 'testusername'

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            username=username
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """Test if user email is normalized after registeration"""
        sample_emails = [
            ['test1@Example.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        i = 1
        for email, expected in sample_emails:
            i += 1
            user = get_user_model().objects.create_user(
                email=email,
                password='testpass',
                username=f'testusername{i}'
            )

            self.assertEqual(user.email, expected)

    def test_user_empty_email_raises_error(self):
        """Test if the user not provide an eamil, raises ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'testpass')

    def test_user_empty_username_raises_error(self):
        """Test if user not provide a username it will raises ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='test@example.com',
                password='testpass',
                username=''
            )

    def test_create_super_user(self):
        """Test create superuser."""
        user = get_user_model().objects.create_superuser(
            email='superuser@example.com',
            password='testsuperuser',
            username='testusername'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
