from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from adminBlog.views import PostListAPIView
from .serializers import *
from utils import paginations
# Create your views here.
def index(request):
    return HttpResponse("homepage")


def post(request):
    pass

class homePageListAPIView(PostListAPIView):
    serializer_class = GetAllPostSerializerUser
    pagination_class = paginations.CustomPagination3
    print('test')
