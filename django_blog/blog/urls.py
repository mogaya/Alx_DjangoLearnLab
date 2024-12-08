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
    path('post', PostListView.as_view(), name='post-list'),  # /post/
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # /post/<id>/
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # /post/new/
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # /post/<id>/edit/
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('post/<int:pk>/comments/new/', CommentCreateView, name='CommentCreateView'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),

    # Search
    path('search/', views.search_posts, name='search_posts'),
    # path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
    path("tags/<slug:tag_slug>/", views.PostByTagListView.as_view(), name='PostByTagListView')
]