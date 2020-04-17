from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = PostModel
    list_display = ['post_title','is_active', 'is_deleted']
    list_filter = ['user', 'post_title']
    search_fields = ['post_title']
    readonly_fields = ['is_active', 'is_deleted']


class CommentsAdmin(admin.ModelAdmin):
    model = CommentsModel
    list_display = ['comment', 'is_deleted', 'is_active']
    list_filter = ['comment']
    search_fields = ['comment']
    readonly_fields = ['is_active', 'is_deleted']

admin.site.register(PostModel, PostAdmin)
admin.site.register(CommentsModel,CommentsAdmin)
