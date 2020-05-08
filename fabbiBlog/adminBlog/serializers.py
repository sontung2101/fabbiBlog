# serializers.py
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from home.models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class PostSerializer(ModelSerializer):
    categories = CategorySerializer(many=True,read_only=True)
    class Meta:
        model = PostModel
        fields = '__all__'
