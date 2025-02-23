from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from relationship_app.view.admin_view import admin_dashboard
from relationship_app.view.librarian_view import librarian_dashboard
from relationship_app.view.member_view import member_dashboard

urlpatterns = [
    path("books/", list_books, name="list_books"), 
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    path("librarian-dashboard/", librarian_dashboard, name="librarian_dashboard"),
    path("member-dashboard/", member_dashboard, name="member_dashboard"),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
]