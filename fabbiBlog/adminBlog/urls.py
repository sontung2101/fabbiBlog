from django.urls import path
from .views import *
app_name = 'adminBlog'
urlpatterns = [
    path('create_user',createUser, name='create-user'),
    path('reset_password', reset_password, name='reset_pasword'),
    path('get_post_list', getPostList, name='get-post-list'),
    path('get_post/<int:id>', getPost, name='get-post'),
    path('create_post', createPost, name='create-post'),
    path('update_post/<int:id>',updatePost,name='update-post'),
    path('get_all_categories',getAllCategories,name='get-all-categories'),
]
