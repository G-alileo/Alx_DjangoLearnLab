from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(TestCase):
    """Test suite for Book API endpoints"""

    def setUp(self):
        """Set up test client and test data"""
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.admin = User.objects.create_superuser(username='admin', password='adminpass')

        # Create an author
        self.author = Author.objects.create(name="Author One") 

        # Create test books using the Author instance
        self.book1 = Book.objects.create(title="Book One", author=self.author, publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author=self.author, publication_year=2021)


        # Authenticate as admin
        self.client.login(username='admin', password='adminpass')

        # Authentication credentials
        self.client.login(username='testuser', password='testpass')

    def test_list_books(self):
        """Test retrieving book list"""
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        """Test creating a new book"""
        self.client.logout()
        self.client.login(username='admin', password='adminpass')
        data = {"title": "New Book", "author": self.author.id, "publication_year": 2023}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_retrieve_book(self):
        """Test retrieving a single book"""
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book One")

    def test_update_book(self):
        """Test updating an existing book"""
        data = {"title": "Updated Book", "author": self.author.id, "publication_year": 2022}
        response = self.client.put(f'/api/books/update/{self.book1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book(self):
        """Test deleting a book"""
        self.client.logout()
        self.client.login(username='admin', password='adminpass')
        response = self.client.delete(f'/api/books/delete/{self.book2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_unauthenticated_access(self):
        """Test that unauthenticated users cannot create books"""
        self.client.logout()
        data = {"title": "Unauthorized Book", "author": "No Access", "publication_year": 2024}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_delete_book(self):
        """Test that only admin users can delete books"""
        self.client.logout()
        self.client.login(username='admin', password='adminpass')
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

