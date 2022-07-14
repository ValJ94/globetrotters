from django.urls import path
from globe_app import views

app_name = 'globe_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register_contd/', views.register_contd, name='register_contd'),
    # path('profile/', views.testFunction, name='profile'),
    # path('profile/<str:username>/', views.testFunction, name='profile'),
    # path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    # path('profile/', views.profile, name='profile'),
    path('profile/<username>/', views.profile, name='profile'),


]