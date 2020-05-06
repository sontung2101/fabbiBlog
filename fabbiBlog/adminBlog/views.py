from rest_framework.decorators import api_view
from rest_framework.response import Response
import re
from .models import *

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
        myUser.objects.create_user(email=email,username=username, password=password)
        return Response({'success': True})
    else:
        return Response({'success': False, 'errors': errors})


def reset_password(request):
    pass