from django.test import TestCase
from django.urls import reverse
from .models import User, ForumPost
from django.contrib.auth import get_user_model



class DestinationMethodTests(TestCase):
    def test_destination_has_location_and_coordinates(self):
        pass




class UserTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

        # self.forumObject = ForumPost.objects.create(writer=self.user,title='Test Title For NOwW',content='Test Content TTT')

    def test_user_exists(self):
        user_count = User.objects.all().count()
        print(user_count)
        self.assertNotEqual(user_count, 0)