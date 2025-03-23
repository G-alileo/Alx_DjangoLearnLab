from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView, PostsByTagView, SearchPostsView

urlpatterns = [

    path('', views.home, name='home'), 
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.posts, name='posts'),
    
    path('posts/', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post

    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    # path('post/<int:post_id>/comment/new/', CommentCreateView.as_view(), name='comment-add'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    path('tags/<str:tag_name>/', PostsByTagView.as_view(), name='posts_by_tag'),
    path('search/', SearchPostsView.as_view(), name='search_posts'),
]
