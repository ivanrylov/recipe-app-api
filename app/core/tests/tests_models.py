from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@gmail.com', password='pass1234'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_sucessful(self):
        """Test creating a user with an email is successful"""
        email = 'test@gmail.com'
        password = 'test123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_emails(self):
        """Test new user creating with no email raised error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creation of superuser"""
        user = get_user_model().objects.create_superuser(
            "test@gmail.com",
            "123test"
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
