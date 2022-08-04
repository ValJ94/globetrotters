from django.urls import path
from globe_app import views

app_name = 'globe_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register_contd/', views.register_contd, name='register_contd'),
    path('profile/<username>/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('find_buddy/', views.find_buddy, name='find_buddy'),
    path('upcoming_travels/<owner>/', views.upcoming_travels, name='upcoming_travels'),
    path('travel_history/', views.travel_history, name='travel_history'),
    path('travel_wishlist/', views.travel_wishlist, name='travel_wishlist'),
    path('travel_notes/', views.travel_notes, name='travel_notes'),
    path('my_trips/', views.my_trips, name='my_trips'),
    path('save_location/', views.save_location, name='save_location'),
    path('get_user_saved_locations/<user>/', views.get_user_saved_locations, name='get_user_saved_locations'),
    path('add_upcoming_travel/', views.add_upcoming_travel, name='add_upcoming_travel'),
    path('buddy_search_results/', views.buddy_search_results, name='buddy_search_results'),
    path('inbox/', views.list_threads, name='inbox'),
    path('inbox/create_thread/', views.CreateThread.as_view(), name='create_thread'),
    path('inbox/<int:pk>/', views.thread_view, name='thread'),
    path('inbox/<int:pk>/create_message/', views.create_message, name='create_message'),

    # New ones for contacting new buddy
    path('inbox/<username>/create_or_find_message_thread/<receiver>/', views.create_or_find_message_thread, name='create_or_find_message_thread'),

]