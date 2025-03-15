from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # This is my nested serializer

    class Meta:
        model = Author
        fields = ['name', 'books']
