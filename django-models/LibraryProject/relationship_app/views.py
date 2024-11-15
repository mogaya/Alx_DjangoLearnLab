from typing import Any
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View

from django.contrib.auth.decorators import user_passes_test

from .models import Book
from .models import Library

# Create your views here.

# Create a function-based view in relationship_app/views.py that lists all books stored in the database.
# This view should render a simple text list of book titles and their authors.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.
# Utilize Django’s ListView or DetailView to structure this class-based view.

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Utilize Django’s built-in views and forms for handling user authentication. You will need to create views for user login, logout, and registration.

# # Login View
# class LoginView(LoginView):
#     template_name = 'relationship_app/login.html'

# # Logout
# class LogoutView(LogoutView):
#     template_name = 'relationship_app.logout.html'

# Registration
class register(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        return render(request, 'relationship_app/register.html', {'form': form})
    
# Role Based Views
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')