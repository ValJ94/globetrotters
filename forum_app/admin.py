from django.contrib import admin
from .models import ForumPost, PostReply

# Register your models here.

admin.site.register(ForumPost)
admin.site.register(PostReply)