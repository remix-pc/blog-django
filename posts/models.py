from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.resize_image(self.imagePost.name, 800)

    @staticmethod
    def resize_image(imageName, newWidth):
        imgPath = os.path.join(settings.MEDIA_ROOT, imageName)
        img = Image.open(imgPath)
        width, height = img.size
        newHeight = round((newWidth * height) / width)

        if width <= newWidth:
            img.close()
            return

        newImage = img.resize((newWidth, newHeight), Image.ANTIALIAS)
        newImage.save(imgPath, optimize=True, quality=60)

        newImage.close()


    

