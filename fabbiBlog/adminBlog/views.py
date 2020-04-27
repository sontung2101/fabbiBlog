from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'adminBlog/login.html')


def register(request):
    return render(request, 'adminBlog/register.html')


def reset_password(request):
    return render(request, 'adminBlog/reset-password.html')
