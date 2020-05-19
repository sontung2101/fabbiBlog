from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
import re
from .models import *
from home.models import *
from .serializers import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from utils import paginations
from rest_framework.views import APIView


# Create your views here.
@api_view(['POST'])
def createUser(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    errors = []
    if myUser.objects.filter(username=username):
        errors.append('Tên tài khoản đã tồn tại')
    if username.strip() == '':
        errors.append('Tên tài khoản không được trống')
    if myUser.objects.filter(email=email):
        errors.append('Email đã tồn tại')
    if not (re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", email) != None):
        errors.append('Email không hợp lệ')
    if len(password) < 6:
        errors.append('Mật khẩu quá ngắn')
    if len(errors) == 0:
        myUser.objects.create_user(email=email, username=username, password=password)
        return Response({'success': True})
    else:
        return Response({'success': False, 'errors': errors})


class PostListAPIView(ListAPIView):
    queryset = PostModel.objects.all().order_by('-created_at')
    serializer_class = GetAllPostSerializer
    pagination_class = paginations.CustomPagination2


@api_view(['GET'])
def getPost(request, id):
    post = PostModel.objects.get(id=id)
    serializers = GetPostSerializer(post)
    return Response(serializers.data)


@api_view(['PUT'])
def updatePost(request, id):
    post = PostModel.objects.get(id=id)
    if request.data['categories'] is not None:
        post.categories.clear()
    serializer = PostSerializer(data=request.data, instance=post, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True})
    else:
        return Response({'success': False, 'errors': serializer.errors})


@api_view(['POST'])
def createPost(requeset):
    serializers = PostSerializer(data=requeset.data)
    if serializers.is_valid():
        serializers.save()
        return Response({"success": True})
    else:
        return Response({"success": False, "errors": serializers.errors})


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAllCategories(request):
    categories = CategoryModel.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request):
    id = request.user.id
    username = request.user.username
    email = request.user.email
    try:
        author = UserProfile.objects.get(user_id=id)
        photo = str(author.photo)
        add = author.address
        gender = author.gender
        phone = author.phone
        data = {
            'author_id': author.id,
            'author_name': username,
            'author_email': email,
            'author_photo': photo,
            'author_add': add,
            'author_gender': gender,
            'author_phone': phone,
        }
        return Response(data)
    except Exception as e:
        return Response({"success": False})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAuthor(request, id):
    author = UserProfile.objects.get(id=id)
    if author:
        myUserId = author.user_id
        author_name = myUser.objects.get(id=myUserId)
        data = {
            'author_name': author_name.username
        }
        return Response(data)
    else:
        return Response({'success': False})


@api_view(['DELETE'])
def deletePost(request, id):
    post = PostModel.objects.get(id=id)
    post.delete()
    return Response({'success': True})


def reset_password(request):
    pass


# ------------------------------------Categories--------------------------------------------
class CategoryListAPIView(ListAPIView):
    queryset = CategoryModel.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    pagination_class = paginations.CustomPagination2


@api_view(['GET'])
def getCategory(request, id):
    category = CategoryModel.objects.get(id=id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['POST'])
def createCategory(request):
    serializers = CategorySerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response({'success': True})
    else:
        return Response({'success': False, 'errors': serializers.errors})


@api_view(['PUT'])
def updateCategory(request, id):
    category = CategoryModel.objects.get(id=id)
    serializer = CategorySerializer(data=request.data, instance=category)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True})
    else:
        return Response({'success': False, 'errorrs': serializer.errors})


@api_view(['DELETE'])
def deleteCategory(request, id):
    category = CategoryModel.objects.get(id=id)
    category.delete()
    return Response({'success': True})
# ---------------------------UserProfile----------------------------------
