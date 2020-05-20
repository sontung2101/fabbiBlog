# serializers.py
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from home.models import *
from django.contrib.auth.password_validation import validate_password


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class GetPostSerializer(ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'


class GetAllPostSerializer(ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = PostModel
        fields = '__all__'


class PostSerializer(ModelSerializer):
    categories = serializers.CharField()

    class Meta:
        model = PostModel
        fields = '__all__'

    def validate_categories(self, attrs):
        return attrs

    def create(self, validated_data):
        categories = validated_data.pop('categories')
        categories = categories.split(',')
        posts = PostModel()
        posts.title = validated_data.pop('title')
        posts.author = validated_data.pop('author')
        posts.sapo = validated_data.pop('sapo')
        posts.content = validated_data.pop('content')
        posts.thumbnail = validated_data.pop('thumbnail')
        posts.save()
        for cate in categories:
            posts.categories.add(cate)
        return posts

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.sapo = validated_data.get('sapo', instance.sapo)
        instance.content = validated_data.get('content', instance.content)
        instance.thumbnail = validated_data.get('thumbnail', instance.thumbnail)
        instance.save()
        categories = validated_data.get('categories')
        categories = categories.split(',')
        for cate_id in categories:
            instance.categories.add(CategoryModel.objects.get(id=cate_id))
        return instance


class MyUserSerialiser(ModelSerializer):
    class Meta:
        model = myUser
        fields = '__all__'


class UserProfileSerializer(ModelSerializer):
    user = MyUserSerialiser(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
