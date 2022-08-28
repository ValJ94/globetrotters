from django.urls import path
from globe_app import views

app_name = 'globe_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register_contd/', views.register_contd, name='register_contd'),
    path('profile/<username>/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('find_buddy/', views.find_buddy, name='find_buddy'),

    # Upcoming Travels
    path('upcoming_travels/<owner>/', views.upcoming_travels, name='upcoming_travels'),
    path('add_upcoming_travel/', views.add_upcoming_travel, name='add_upcoming_travel'),
    path('save_location/', views.save_location, name='save_location'),
    path('get_user_saved_locations/<user>/', views.get_user_saved_locations, name='get_user_saved_locations'),

    # Travel History
    path('travel_history/<owner>/', views.travel_history, name='travel_history'),
    path('add_history/', views.add_history, name='add_history'),
    path('save_history_location/', views.save_history_location, name='save_history_location'),
    path('get_user_saved_history_locations/<user>/', views.get_user_saved_history_locations, name='get_user_saved_history_locations'),

    # Travel Wishlist
    path('travel_wishlist/<owner>/', views.travel_wishlist, name='travel_wishlist'),
    path('add_wishlist/', views.add_wishlist, name='add_wishlist'),
    path('save_wishlist_location/', views.save_wishlist_location, name='save_wishlist_location'),
    path('get_user_saved_wishlist_locations/<user>/', views.get_user_saved_wishlist_locations, name='get_user_saved_wishlist_locations'),
    
    path('my_trips/', views.my_trips, name='my_trips'),
    path('search_users/', views.search_users, name='search_users'),

    # Messaging URLs
    path('inbox/', views.list_threads, name='inbox'),
    path('inbox/<int:pk>/', views.thread_view, name='thread'),
    path('inbox/<int:pk>/create_message/', views.create_message, name='create_message'),
    path('inbox/<username>/create_or_find_message_thread/<receiver>/', views.create_or_find_message_thread, name='create_or_find_message_thread'),

]