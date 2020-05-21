from django.urls import path
from .views import *
app_name = 'home'
urlpatterns = [
    path('', homePageListAPIView.as_view(), name='index2'),
    path('get_post/<int:id>', getPost, name='get-post'),
    path('get_categories',getCategoriesViewUser,name='get-categories'),
]
