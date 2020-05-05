from django.urls import path
from .views import *
app_name = 'adminBlog'
urlpatterns = [
    path('login', Login, name='login'),
    path('create_user',createUser, name='create-user'),
    path('hello',hello, name='hello'),
    path('reset_password', reset_password, name='reset_pasword'),
]
