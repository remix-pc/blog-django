from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titlePost', 'author', 'date', 'category', 'publishPost')
    list_editable = ('publishPost',)
    list_display_links = ('id', 'titlePost',)



admin.site.register(Post, PostAdmin)