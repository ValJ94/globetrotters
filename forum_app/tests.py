from django.test import TestCase
from django.urls import reverse
from .models import ForumPost, PostReply
from globe_app.models import User
from django.contrib.auth import get_user_model


class ForumViewTests(TestCase):
    def test_forum_view_with_no_posts(self):
        response = self.client.get(reverse('forum_app:forum'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no posts currently.')
        self.assertQuerysetEqual(response.context['post_list'], [])


class PostViewTests(TestCase):
    def test_post_view_with_no_replies(self):
        response = self.client.get(f'/forum/{self.forumObject.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no comments for this post.')
        self.assertQuerysetEqual(response.context['post_replies'], [])


    # def test_post_view_with_replies(self):
    #     reply1 = PostReply.objects.create(reply_writer=self.user, content='Content for Reply 1')
    #     reply2 = PostReply.objects.create(reply_writer=self.user, content='Content for Reply 2')

    #     response = self.client.get(f'/forum/{self.forumObject.id}/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, reply1)
    #     self.assertContains(response, reply2)

    #     num_replies = len(response.context['post_replies'])
    #     self.assertEquals(num_replies, 2)



    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

        self.forumObject = ForumPost.objects.create(writer=self.user,title='Test Title For NOwW',content='Test Content TTT')

    # def test_user_exists(self):
    #     user_count = User.objects.all().count()
    #     print(user_count)
    #     self.assertNotEqual(user_count, 0)