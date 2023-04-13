from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'titlePost', 'author', 'date', 'category', 'publishPost')
    list_editable = ('publishPost',)
    list_display_links = ('id', 'titlePost',)
    summernote_fields = ('content', )


admin.site.register(Post, PostAdmin)