from django.test import Client
from csv import writer
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

    def test_forum_view_with_posts(self):
        title = 'this is a title'
        content = 'this is content'
        add_post(self.user, title, content)

        response = self.client.get(reverse('forum_app:forum'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "this is a title")

        num_posts = len(response.context['post_list'])
        self.assertEquals(num_posts, 1)


    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

def add_post(user, title, content):
    post = ForumPost.objects.get_or_create(writer=user)[0]
    post.title = title
    post.content = content
    post.save()

    return post


class PostViewTests(TestCase):
    def test_post_view_with_no_replies(self):
        response = self.client.get(f'/forum/{self.postObject.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no comments for this post.')
        self.assertQuerysetEqual(response.context['post_replies'], [])


    def test_post_view_with_replies(self):
        title = 'this is a title'
        content = 'this is content'
        add_reply(self.postObject, self.user, title, content)

        response = self.client.get(f'/forum/{self.postObject.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'this is content')

        num_replies = len(response.context['post_replies'])
        self.assertEquals(num_replies, 1)



    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

        self.postObject = ForumPost.objects.create(writer=self.user,title='Test Title For NOwW',content='Test Content TTT')


def add_reply(post, user, title, content):
    reply = PostReply.objects.get_or_create(reply_writer=user, post=post)[0]
    reply.title = title
    reply.content = content

    reply.save()
    return reply


class PostFormTest(TestCase):
    def test_add_post_form_not_filled(self):
        response = self.client.post('/forum/add_post/', data={})
        self.assertEqual(response.status_code, 200)
    
    def test_add_post_form_filled(self):
        response = self.client.post('/forum/add_post/', data={'content': "Testing content", 'title':'Hi'})
        self.assertEqual(response.status_code, 302)

    def test_add_post_form_not_filled_get_request(self):
        response = self.client.get('/forum/add_post/', data={})
        self.assertEqual(response.status_code, 200)

    def test_add_post_form_filled_get_request(self):
        response = self.client.get('/forum/add_post/', data={'content': "Testing content", 'title':'Hi'})
        self.assertEqual(response.status_code, 200)



    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

        self.postObject = ForumPost.objects.create(writer=self.user,title='Test Title For NOwW',content='Test Content TTT')

        # user = User.objects.create(username='testuser', password='12345')

        self.client = Client()
        self.logged_in = self.client.login(username='myusername', password='foo')


class ReplyFormTest(TestCase):
    def test_add_reply_form_not_filled(self):
        response = self.client.post(f'/forum/{self.postObject.id}/add_reply', data={})
        self.assertEqual(response.status_code, 301)
    
    def test_add_reply_form_filled(self):
        response = self.client.post(f'/forum/{self.postObject.id}/add_reply', data={'content': "Testing content"})
        self.assertEqual(response.status_code, 301)

    def test_add_reply_form_not_filled_get_request(self):
        response = self.client.get(f'/forum/{self.postObject.id}/add_reply', data={})
        self.assertEqual(response.status_code, 301)

    def test_add_reply_form_filled_get_request(self):
        response = self.client.get(f'/forum/{self.postObject.id}/add_reply', data={'content': "Testing content"})
        self.assertEqual(response.status_code, 301)


    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

        self.postObject = ForumPost.objects.create(writer=self.user,title='Test Title For NOwW',content='Test Content TTT')

        self.client = Client()
        self.logged_in = self.client.login(username='myusername', password='foo')