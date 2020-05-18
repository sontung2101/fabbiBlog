from django.urls import path
from .views import *

app_name = 'adminBlog'
urlpatterns = [
    path('create_user', createUser, name='create-user'),
    path('reset_password', reset_password, name='reset_pasword'),
    path('get_post_list', PostListAPIView.as_view(), name='get-post-list'),
    path('get_post/<int:id>', getPost, name='get-post'),
    path('create_post', createPost, name='create-post'),
    path('update_post/<int:id>', updatePost, name='update-post'),
    path('get_all_categories', getAllCategories, name='get-all-categories'),
    path('get_user', getUser, name='get-user'),
    path('get_author/<int:id>', getAuthor, name='get-author'),
    path('delete_post/<int:id>', deletePost, name='delete-post'),
    # --------------------Categories-----------------------------
    path('get_category/<int:id>', getCategory, name='get-category'),
    path('create_category',createCategory,name='create-category'),
    path('update_category/<int:id>',updateCategory,name = 'update-category'),
    path('delete_category/<int:id>',deleteCategory,name = 'delete-category'),


]