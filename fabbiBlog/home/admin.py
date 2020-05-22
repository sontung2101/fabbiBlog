from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = PostModel
    list_display = ['title','is_active', 'is_deleted']
    list_filter = ['is_active']
    search_fields = ['post_title']
    readonly_fields = ['is_active', 'is_deleted']


class CommentsAdmin(admin.ModelAdmin):
    model = CommentsModel
    list_display = ['content', 'is_deleted', 'is_active']
    list_filter = ['is_active']
    search_fields = ['content']
    readonly_fields = ['is_active', 'is_deleted']

admin.site.register(CategoryModel)
admin.site.register(UploadModel)
admin.site.register(PostModel, PostAdmin)
admin.site.register(CommentsModel,CommentsAdmin)
