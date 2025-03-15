from rest_framework import serializers
from .models import Author, Book
from datetime import date


# Serializes all book fields.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Ensuring that the publication year is not greater than current date
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializes the author's name and uses nested serialization to include related books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # This is my nested serializer

    class Meta:
        model = Author
        fields = ['name', 'books']
