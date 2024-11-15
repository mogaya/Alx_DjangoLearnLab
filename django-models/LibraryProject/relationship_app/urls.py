# Edit relationship_app/urls.py to include URL patterns that route to the newly created views. Make sure to link both the function-based and class-based views.

from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('', list_books, name='list_books'),
    path('library/<int:pk>', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]