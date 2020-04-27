from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def post(request):
    return render(request, 'home/post.html')


def login(requset):
    return render(requset, 'admin/login.html')


def register(requset):
    return render(requset, 'admin/register.html')
