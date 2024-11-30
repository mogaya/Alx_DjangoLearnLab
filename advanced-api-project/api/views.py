from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
# from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework

# Create your views here.
# ListView - Retrieve all books.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    # Add filtering, searching, and ordering backends
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filter by title, author name, and year
    filterset_fields =['title', 'author__name', 'publication_year']

    search_fields = ['title', 'author__name']

    ordering_fields = ['title', 'publication_year']

# DetailView - Retrieve a single book by ID.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView - Add a new book.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# UpdateView - Modify an existing book.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# DeleteView - Remove a book.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]