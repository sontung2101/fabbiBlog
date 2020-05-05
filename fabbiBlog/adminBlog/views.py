from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *



# Create your views here.
@api_view(['GET'])
def Login(request):
    pass

@api_view(['POST'])
def createUser(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    errors = []
    if len(password) < 6:
        errors.append('Mật khẩu quá ngắn')
    if myUser.objects.filter(email=email):
        errors.append('Email đã tồn tại')
    if myUser.objects.filter(username=username):
        errors.append('Tên tài khoản đã tồn tại')
    if username.strip() == '':
        errors.append('Tên tài khoản không được trống')
    if email.strip() == '':
        errors.append('Email không được trống')
    if len(errors) == 0:
        myUser.objects.create_user(email=email,username=username, password=password)
        return Response({'success': True})
    else:
        return Response({'success': False, 'errors': errors})


def reset_password(request):
    pass
@api_view(['GET','POST'])
def hello(request):
    return Response({'message':'Hello'})