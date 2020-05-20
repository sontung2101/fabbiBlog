from django.urls import path
from .views import *
app_name = 'home'
urlpatterns = [
    path('', homePageListAPIView.as_view(), name='index'),
    path('post', post, name='post'),
]
