from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')
def post(request):
    return render(request,'post.html')