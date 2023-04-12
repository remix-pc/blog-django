from django.db import models

# Create your models here.


class Category(models.Model):
    name_cat = models.CharField(max_length=50)
    