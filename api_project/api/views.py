from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  #Allow any user to access


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access