# Edit relationship_app/urls.py to include URL patterns that route to the newly created views. Make sure to link both the function-based and class-based views.

from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', list_books, name='list_books'),
    path('library/<int:pk>', LibraryDetailView.as_view(), name='library_detail'),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.register.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name= 'relationship_app/login.html'), name='login' ),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app.logout.html'), name='logout'),

    path('admin/', views.admin_view, name ='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    path('add_book/', views.add_book, name='add_book'),  # URL for adding a book
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
]