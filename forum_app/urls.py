from django.urls import path
from forum_app import views

app_name = 'forum_app'

urlpatterns = [
    path('', views.forum, name='forum'),
    path('add_post/', views.add_post, name='add_post'),
    path('<int:id>/', views.view_post, name='view_post'),
    path('add_reply/', views.add_reply, name='add_reply'),
]