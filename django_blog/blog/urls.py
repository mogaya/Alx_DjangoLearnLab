from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView
)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Update
    path('post', PostListView.as_view(), name='post-list'),  # /posts/
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # /posts/<id>/
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # /posts/new/
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),  # /posts/<id>/edit/
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]