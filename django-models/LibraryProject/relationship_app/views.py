from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from relationship_app.decorator import role_required

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

class UserLoginView(LoginView):
    template_name = "relationship_app/login.html"

class UserLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect("home") 
    else:
        form = UserCreationForm()
    
    return render(request, "relationship_app/register.html", {"form": form})

@login_required
@role_required('ADMIN')
def admin_view(request):
    return render(request, 'admin_dashboard.html', {
        'title': 'Admin Dashboard',
        'content': 'Welcome to the Admin Dashboard'
    })

@login_required
@role_required('LIBRARIAN')
def librarian_view(request):
    return render(request, 'librarian_dashboard.html', {
        'title': 'Librarian Dashboard',
        'content': 'Welcome to the Librarian Dashboard'
    })

@login_required
@role_required('MEMBER')
def member_view(request):
    return render(request, 'member_dashboard.html', {
        'title': 'Member Dashboard',
        'content': 'Welcome to the Member Dashboard'
    })
