from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def posts(request):
    return render(request, 'blog/posts.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')  # Redirect to home page after login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    else:
        form = AuthenticationForm()
    
    return render(request, 'blog/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'blog/profile.html')


# List all blog posts (publicly accessible)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Template for displaying posts
    context_object_name = 'posts'
    ordering = ['-date_posted']  # Show latest posts first

# Show a single post (publicly accessible)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# Create a new blog post (only for authenticated users)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

# Update a blog post (only for the author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can edit

# Delete a blog post (only for the author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')  # Redirect to list view after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can delete