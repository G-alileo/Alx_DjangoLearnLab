from bookshelf.models import Book
# Create a new Book instance
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Output: <Book: 1984>

