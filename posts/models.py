from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    titlePost = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    excerpt = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    imagePost = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True)
    publishPost = models.BooleanField(default=False)

    

