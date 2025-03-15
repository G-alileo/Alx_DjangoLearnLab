from django.contrib import admin
from .models import Author, Book

# Register your models here.

# admin.site.register(Author)
# admin.site.register(Book)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_year', 'author')
    list_filter = ('publication_year', 'author')
    search_fields = ('title',)