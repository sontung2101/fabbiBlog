from django.db import models
from django.contrib.auth.models import User
from adminBlog.models import *
from tinymce.models import HTMLField
from adminBlog.models import *


# Create your models here.
# Create your models here.

class CategoryModel(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'

    def __str__(self):
        return self.title


class PostModel(models.Model):
    title = models.CharField(max_length=100, unique=True)
    sapo = models.CharField(max_length=200,blank=True)
    content = HTMLField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='uploads', blank=False)
    categories = models.ManyToManyField(CategoryModel)
    is_active = models.BooleanField(null=True, blank=True, default=True)
    is_deleted = models.BooleanField(null=True, blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'

    def __str__(self):
        return self.title


class CommentsModel(models.Model):
    user = models.ForeignKey(myUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=100,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(PostModel, related_name='comments', on_delete=models.CASCADE)
    is_active = models.BooleanField(null=True, blank=True, default=True)
    is_deleted = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        verbose_name = 'Comments'

    def __str__(self):
        return self.user
