from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Step 1: Create a ViewSet
# ViewSets in DRF allow you to consolidate common logic for handling standard operations into a single class that handles all HTTP methods (GET, POST, PUT, DELETE).

# Define the ViewSet:
# In api/views.py, extend the existing view setup by adding a new class BookViewSet that handles all CRUD operations.
# Use rest_framework.viewsets.ModelViewSet, which provides implementations for various actions like list, create, retrieve, update, and destroy.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer