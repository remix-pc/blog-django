from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    nameComment = models.CharField(max_length=150)
    emailComment = models.EmailField()
    comment = models.TextField()
    postComment = models.ForeignKey(Post, on_delete=models.CASCADE)
    userComment = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateComment = models.DateTimeField(default=timezone.now)
    publishComment = models.BooleanField(default=False)

    def __str__(self):
        return self.nameComment