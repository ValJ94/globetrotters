from django.urls import path
from globe_app import views

app_name = 'globe_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register_contd/', views.register_contd, name='register_contd'),
    path('profile/<username>/', views.profile, name='profile'),
    path('forum/', views.forum, name='forum'),
    path('about/', views.about, name='about'),
    path('find_buddy/', views.find_buddy, name='find_buddy'),
    path('upcoming_travels/', views.upcoming_travels, name='upcoming_travels'),
    path('travel_history/', views.travel_history, name='travel_history'),
    path('travel_wishlist/', views.travel_wishlist, name='travel_wishlist'),
    path('travel_notes/', views.travel_notes, name='travel_notes'),
    path('my_trips/', views.my_trips, name='my_trips'),
]