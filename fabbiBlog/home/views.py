from django.shortcuts import render, HttpResponse, redirect
from .models import PostModel, CommentsModel
import requests


# Create your views here.
def index(request):
    url = ""
    data = requests.get(url).json()
    return render(request, '../templates/home/index.html', {'Posts': data})


def post(request):
    url = ""
    data = requests.get(url).json()
    comments = requests.get(url).json()
    if request.method == "POST":
        if "add_comment" in request.POST:
            content = request.POST["content"]
            new_comment = CommentsModel(content=content)
            requests.post(url, new_comment.json())
            return redirect("/")
    return render(request, '../templates/home/post_detail.html', {'Post': data}, {'Comments': comments})
