from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from home.models import *
from adminBlog.serializers import CategorySerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = myUser
        fields=('username',)

class AuthorSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ('user',)
class GetAllPostSerializerUser(ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = PostModel
        fields = '__all__'
