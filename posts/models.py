from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    titlePost = models.CharField(max_length=255, verbose_name="Title")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Author")
    date = models.DateTimeField(default=timezone.now, verbose_name="Date")
    content = models.TextField(verbose_name="Content")
    excerpt = models.TextField(verbose_name="Excerpt")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="Category")
    imagePost = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name="Image")
    publishPost = models.BooleanField(default=False, verbose_name="Publish")

    def __str__(self):
        return self.titlePost

    

