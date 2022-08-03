from django.db import models
from globe_app.models import User
from django.utils import timezone


CharMaxLength = 200

class ForumPost(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=CharMaxLength)
    content = models.TextField()
    
    def __str__(self):
        return self.title

class PostReply(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    reply_writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'post replies'
