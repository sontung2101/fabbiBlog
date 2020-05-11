from rest_framework.decorators import api_view
from rest_framework.response import Response
import re
from .models import *
from home.models import *
from .serializers import *


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


@api_view(['GET'])
def getPostList(request):
    lst = PostModel.objects.all()
    serializers = PostSerializer(lst, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getPost(request, id):
    post = PostModel.objects.get(id=id)
    serializers = PostSerializer(post)
    return Response(serializers.data)


@api_view(['PUT'])
def updatePost(request,id):
    post = PostModel.objects.get(id=id)
    serializer = PostSerializer(data=request.data, instance=post)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True})
    else:
        return Response({'success': False, 'errors': serializer.errors})


@api_view(['POST'])
def createPost(requeset):
    print(requeset.data)
    serializers = PostSerializer(data=requeset.data)
    if serializers.is_valid():
        serializers.save()
        return Response({"success":True})
    else:
        return Response({"success":False,"errors":serializers.errors})

@api_view(['GET'])
def getAllCategories(request):
    categories = CategoryModel.objects.all()
    serializer = CategorySerializer(categories,many=True)
    return Response(serializer.data)
def reset_password(request):
    pass
