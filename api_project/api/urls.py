from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]