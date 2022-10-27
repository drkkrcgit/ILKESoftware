"""
Test for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an username is successful. """
        username = 'testusername'
        password = 'testpass123'
        user_group = 'testgroup'
        user = get_user_model().objects.create_user(
            username=username,
            user_group=user_group,
            password=password,
        )

        self.assertEqual(user.username, username)
        self.assertEqual(user.user_group, user_group)
        self.assertTrue(user.check_password(password))

    def test_new_user_without_username_raises_error(self):
        """Test that creating a user without a username raises ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                '',
                'testgroup',
                'testpass123'
            )

    def test_new_user_without_user_group_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                'testusername',
                '',
                'testpass123',
            )

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'testsuperuser',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.check_password('test123'))
