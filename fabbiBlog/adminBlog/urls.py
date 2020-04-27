from django.urls import path
from .views import *
app_name = 'adminBlog'
urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('register', register, name='register'),
    path('reset_password', reset_password, name='reset_pasword'),
]
