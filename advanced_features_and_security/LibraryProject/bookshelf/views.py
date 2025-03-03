from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Book
from .forms import BookForm, ExampleForm


# Create your views here.
def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data here
            return redirect('book_list')
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})

# Read operation 
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Using ORM securely to get all books
    books = Book.objects.all()
    
    # Adding search functionality with secure handling
    search_query = request.GET.get('search', '')
    if search_query:
        # Use ORM filtering instead of raw SQL queries
        books = books.filter(title__icontains=search_query) | books.filter(author__icontains=search_query)
    
    return render(request, 'bookshelf/book_list.html', {
        'books': books,
        'search_query': search_query
    })

# Create operation
@permission_required('bookshelf.can_create', raise_exception=True)
@ensure_csrf_cookie  
@require_http_methods(["GET", "POST"])  # Restricts to specific HTTP methods
def book_create(request):
    if request.method == "POST":
        # Use Django forms for validation and sanitization
        form = BookForm(request.POST)
        if form.is_valid():
            # Save form data directly
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()  # Create empty form for GET requests
    
    return render(request, 'bookshelf/book_form.html', {'form': form})

# Update operation
@permission_required('bookshelf.can_edit', raise_exception=True)
@ensure_csrf_cookie  
@require_http_methods(["GET", "POST"]) 
def book_edit(request, book_id):
    # Secure lookup with get_object_or_404
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == "POST":
        # Use form with instance for validation and updating
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)  # Pre-fill form with book data
    
    return render(request, 'bookshelf/book_form.html', {'form': form, 'book': book})

# Delete operation
@permission_required('bookshelf.can_delete', raise_exception=True)
@ensure_csrf_cookie  
@require_http_methods(["GET", "POST"]) 
def book_delete(request, book_id):
    # Secure lookup with get_object_or_404
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})