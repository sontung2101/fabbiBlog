from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'admin/login.html')


def register(request):
    return render(request, 'admin/register.html')


def reset_password(request):
    return render(request, 'admin/reset-password.html')
