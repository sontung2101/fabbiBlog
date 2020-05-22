from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from adminBlog.views import PostListAPIView
from .serializers import *
from utils import paginations


# Create your views here.
def index(request):
    return HttpResponse("homepage")


class homePageListAPIView(PostListAPIView):
    serializer_class = GetAllPostSerializerUser
    pagination_class = paginations.CustomPagination3
    search_fields = ('title', 'author__user__username', 'categories__title')


@api_view(['GET'])
def getCategoriesViewUser(request):
    categories = CategoryModel.objects.all()
    count = categories.count() // 2
    cate2 = categories[:count]
    cate = categories[count:]
    serializer = CategorySerializer(cate, many=True)
    serializer2 = CategorySerializer(cate2, many=True)
    return Response({'cate': serializer.data, 'cate2': serializer2.data})


@api_view(['GET'])
def getPost(request, id):
    try:
        post = PostModel.objects.get(id=id)
        serializer = GetAllPostSerializerUser(post)
        return Response(serializer.data)
    except Exception:
        return Response({'success': False})
