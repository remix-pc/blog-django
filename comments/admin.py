from django.contrib import admin
from .models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'nameComment', 'emailComment', 'postComment', 'dateComment', 'publishComment')
    list_editable = ('publishComment',)
    list_display_links = ('id', 'nameComment', 'emailComment', )


admin.site.register(Comment, CommentAdmin)