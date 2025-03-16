from django.shortcuts import render
from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from django_filters import rest_framework as django_filters

# Create your views here.


# ListView - Retrieve all books (Read-Only)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']  # Enable search on title and author's name
    ordering_fields = ['title', 'publication_year']   # Enable ordering on title and publication year
    ordering = ['title']  # Default ordering

    def get_queryset(self):
        """
        Filters books based on query parameters:
        - title: Filters books containing the given title.
        - author: Filters books by author's name.
        - publication_year: Filters books by the given publication year.
        """
        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        publication_year = self.request.query_params.get('publication_year')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__name__icontains=author)
        if publication_year:
            queryset = queryset.filter(publication_year=publication_year)

        return queryset

# DetailView - Retrieve a single book by ID (Read-Only)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# CreateView - Add a new book (Restricted to Authenticated Users)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# UpdateView - Modify an existing book (Restricted to Authenticated Users)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# DeleteView - Remove a book (Restricted to Admin Users Only)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]