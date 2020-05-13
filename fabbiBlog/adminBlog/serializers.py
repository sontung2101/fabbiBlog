# serializers.py
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from home.models import *


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
        instance.author = validated_data.get('author',instance.author)
        instance.categories = validated_data.get('categories',instance.categories)
        instance.sapo = validated_data.get('sapo',instance.sapo)
        instance.content = validated_data.get('content',instance.content)
        instance.thumbnail = validated_data.get('thumbnail',instance.thumbnail)

        return instance
