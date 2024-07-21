from django.urls import path
from forum_app import views

app_name = 'forum_app'

urlpatterns = [
    path('', views.forum, name='forum'),
    path('add_post/', views.add_post, name='add_post'),
    path('<int:id>/', views.view_post, name='view_post'),
    path('<int:id>/add_reply/', views.reply_view, name='add_reply'),
]