from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    CommentCreateView, 
    CommentUpdateView, 
    CommentDeleteView
)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Posts
    path('post', PostListView.as_view(), name='post-list'),  # /posts/
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # /posts/<id>/
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # /posts/new/
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # /posts/<id>/edit/
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('posts/<int:post_id>/comments/new/', CommentCreateView, name='CommentCreateView'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]