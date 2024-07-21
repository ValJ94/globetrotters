from operator import contains
from django.test import TestCase
from django.urls import reverse
from .forms import ProfileForm, upcomingTravelForm, TravelHistoryForm, TravelWishlistForm
from .filters import BuddyFilter
from .models import Destination, UpcomingTravel, User, ForumPost, UserProfile, MessageThread, Message
from django.contrib.auth import get_user_model
from django.conf import settings
from django.test import Client



class DestinationMethodTests(TestCase):
    def test_destination_has_location_and_coordinates(self):
        pass


class TravelViewTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

        self.destinationObject = Destination.objects.create(locationName='Bolivia', longitude='34.2', latitude='21.2')

        self.client = Client()
        self.logged_in = self.client.login(username='myusername', password='foo')

    def test_upcoming_view(self):
        response = self.client.get(f'/globetrotters/upcoming_travels/{self.user.username}/')
        self.assertEqual(response.status_code, 200)

    def test_add_upcoming_view(self):
        response = self.client.get(f'/globetrotters/add_upcoming_travel/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add a destination')

    def test_history_view(self):
        response = self.client.get(f'/globetrotters/travel_history/{self.user.username}/')
        self.assertEqual(response.status_code, 200)

    def test_add_history_view(self):
        response = self.client.get(f'/globetrotters/add_history/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add a destination')

    def test_wishlist_view(self):
        response = self.client.get(f'/globetrotters/travel_wishlist/{self.user.username}/')
        self.assertEqual(response.status_code, 200)

    def test_add_wishlist_view(self):
        response = self.client.get(f'/globetrotters/add_wishlist/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add a destination')

class UpcomingFormTests(TestCase):
    def test_upcoming_form_not_filled(self):
        form_data = {'user': self.user}
        form = upcomingTravelForm(data=form_data)
        self.assertFalse(form.is_valid())
        response = self.client.post('/globetrotters/add_upcoming_travel', data={})
        self.assertEqual(response.status_code, 301)
    
    def test_upcoming_form_filled(self):
        form_data = {'destination': self.destinationObject, 'dateStart':'2022-07-30', 'dateEnd':'2022-07-30', 'budgetStart':'20', 'budgetEnd': '30', 'travelNotes': 'mynotes'}
        form = upcomingTravelForm(data=form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post('/globetrotters/add_upcoming_travel', data=form_data)
        self.assertEqual(response.status_code, 301)

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

        self.destinationObject = Destination.objects.create(id='1', locationName='Bolivia', longitude='34.2', latitude='21.2')

        self.client = Client()
        self.logged_in = self.client.login(username='myusername', password='foo')


class HistoryFormTests(TestCase):
    def test_history_form_not_filled(self):
        form_data = {'user': self.user}
        form = TravelHistoryForm(data=form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post('/globetrotters/add_history', data={})
        self.assertEqual(response.status_code, 301)
    
    def test_history_form_filled(self):
        form_data = {'destination': self.destinationObject, 'travelNotes': 'mynotes'}
        form = TravelHistoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

        self.destinationObject = Destination.objects.create(id='1', locationName='Bolivia', longitude='34.2', latitude='21.2')

        self.client = Client()
        self.logged_in = self.client.login(username='myusername', password='foo')


class WishlistFormTests(TestCase):
    def test_wishlist_form_not_filled(self):
        form_data = {'user': self.user}
        form = TravelWishlistForm(data=form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post('/globetrotters/add_wishlist', data={})
        self.assertEqual(response.status_code, 301)
    
    def test_wishlist_form_filled(self):
        form_data = {'destination': self.destinationObject, 'travelNotes': 'mynotes'}
        form = TravelWishlistForm(data=form_data)
        self.assertTrue(form.is_valid())

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

        self.destinationObject = Destination.objects.create(id='1', locationName='Bolivia', longitude='34.2', latitude='21.2')

        self.client = Client()
        self.logged_in = self.client.login(username='myusername', password='foo')


class UserTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

        self.profileObject = UserProfile.objects.create(user=self.user, first_name='myfirstname', surname='mysurname', age='20')

        self.client = Client()
        self.logged_in = self.client.login(username='myusername', password='foo')

    def test_user_exists(self):
        user_count = User.objects.all().count()
        print(user_count)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        user = User.objects.filter(username__iexact='myusername')
        user_exists = user.exists() and user.count() == 1
        self.assertTrue(user_exists)
        self.user = user.first()
        self.assertTrue(self.user.check_password('foo'))

    def test_user_profile_view(self):
        response = self.client.get(f'/globetrotters/profile/{self.user.username}/')
        self.assertEqual(response.status_code, 200)

class UserFormTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        self.client = Client()
        self.logged_in = self.client.login(username='myusername', password='foo')

        # self.profileObject = UserProfile.objects.create(user=self.user, first_name='myfirstname', surname='mysurname', age='20')

    def test_register_form_not_filled(self):
        form_data = {'user': self.user}
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())
        response = self.client.post('/globetrotters/register_contd/', data={})
        self.assertEqual(response.status_code, 200)
    
    def test_register_form_filled(self):
        form_data = {'user': self.user, 'first_name':'myfirstname', 'surname':'mysurname', 'age':'20'}
        form = ProfileForm(data=form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post('/globetrotters/register_contd/', data={'user': self.user, 'first_name':'myfirstname', 'surname':'mysurname', 'age':'20'})
        self.assertEqual(response.status_code, 302)


class FindBuddyFilterTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

        self.profileObject = UserProfile.objects.create(user=self.user, first_name='myfirstname', surname='mysurname', age='20')
        self.destinationObject = Destination.objects.create(locationName='Bolivia', longitude='34.2', latitude='21.2')
        # self.upcomingObject = UpcomingTravel.objects.create(owner= self.user, destination=self.destinationObject,
        #                         dateStart='2023-07-30', dateEnd='2023-07-30', budgetStart='20', budgetEnd='30')


        self.client = Client()
        self.logged_in = self.client.login(username='myusername', password='foo')
    
    def test_find_buddy_filter_not_filled(self):
        qs = UpcomingTravel.objects.all()
        filter = BuddyFilter
        self.assertEqual((len(qs) > 0), False)

    def test_find_buddy_filter_filled(self):
        self.upcomingObject = UpcomingTravel.objects.create(owner= self.user, destination=self.destinationObject,
                                dateStart='2023-07-30', dateEnd='2023-07-30', budgetStart='20', budgetEnd='30')

        qs = UpcomingTravel.objects.all()
        filter = BuddyFilter()
        self.assertEqual((len(qs) > 0), True)


class FindBuddyViewTest(TestCase):
    def test_find_buddy_view(self):
        response = self.client.get('/globetrotters/find_buddy')
        self.assertEqual(response.status_code, 301)


class MessageViewTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        self.client = Client()
        self.logged_in = self.client.login(username='myusername', password='foo')


        self.profileObject = UserProfile.objects.create(user=self.user, first_name='myfirstname', surname='mysurname', age='20')


    def test_inbox_no_threads_view(self):
        response = self.client.get('/globetrotters/inbox')
        self.assertEqual(response.status_code, 301)

    def test_inbox_with_threads_view(self):
        user2 = User.objects.create_user(username='receiver', email='receiver@user.com', password='foo')
        self.messageThreadObject = MessageThread.objects.create(user=self.user, receiver=user2)

        mt = MessageThread.objects.all()

        self.assertEqual((len(mt) >0), True)
        

class MessageFormTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='myusername', email='normal@user.com', password='foo')
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        self.client = Client()
        self.logged_in = self.client.login(username='myusername', password='foo')

        self.profileObject = UserProfile.objects.create(user=self.user, first_name='myfirstname', surname='mysurname', age='20')

    def test_message_form_not_filled(self):
        user2 = User.objects.create_user(username='receiver', email='receiver@user.com', password='foo')
        self.threadObject = MessageThread.objects.create(user=self.user, receiver=user2)

        response = self.client.post(f'/globetrotters/inbox/{self.threadObject.pk}/', data={})
        self.assertEqual(response.status_code, 200)
    
    def test_message_form_filled(self):
        user2 = User.objects.create_user(username='receiver', email='receiver@user.com', password='foo')
        self.threadObject = MessageThread.objects.create(user=self.user, receiver=user2)

        response = self.client.post(f'/globetrotters/inbox/{self.threadObject.pk}/', data={'content': "Testing content"})
        self.assertEqual(response.status_code, 200)

    def test_message_form_not_filled_get_request(self):
        user2 = User.objects.create_user(username='receiver', email='receiver@user.com', password='foo')
        self.threadObject = MessageThread.objects.create(user=self.user, receiver=user2)

        response = self.client.get(f'/globetrotters/inbox/{self.threadObject.pk}/', data={})
        self.assertEqual(response.status_code, 200)

    def test_message_form_filled_get_request(self):
        user2 = User.objects.create_user(username='receiver', email='receiver@user.com', password='foo')
        self.threadObject = MessageThread.objects.create(user=self.user, receiver=user2)
        
        response = self.client.get(f'/globetrotters/inbox/{self.threadObject.pk}/', data={'content': "Testing content"})
        self.assertEqual(response.status_code, 200)

class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get('/globetrotters/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'want to travel alone?')

class AboutViewTest(TestCase):
    def test_about_view(self):
        response = self.client.get('/globetrotters/about/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to Globetrotters!')

class SearchUsersViewTest(TestCase):
    def test_search_view(self):
        response = self.client.get('/globetrotters/search_users/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Results for')