from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts, name="posts"),
    # path('', PostListView.as_view(), name='posts'),
    # path('post/<int:pk>', post, name='post_detail'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('post/new/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('comment/<int:pk>/', comment_detail, name='comment_detail'),
    path('comments/', comment_list, name='comment_list'),
]
