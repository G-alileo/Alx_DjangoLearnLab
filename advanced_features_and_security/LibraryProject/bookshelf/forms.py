from django import forms
from .models import Book
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class BookForm(forms.ModelForm):
    # Add validators explicitly for each field
    title = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    author = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    # Add validation for year (must be a reasonable year)
    current_year = datetime.datetime.now().year
    publication_year = forms.IntegerField(
        validators=[
            MinValueValidator(1000, message="Year must be at least 1000"),
            MaxValueValidator(current_year, message=f"Year cannot be in the future (current year: {current_year})")
        ],
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        
    # Custom validation for title field
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and len(title.strip()) < 2:
            raise forms.ValidationError("Title must be at least 2 characters long")
        return title
    
    # Custom validation for author field
    def clean_author(self):
        author = self.cleaned_data.get('author')
        if author and len(author.strip()) < 2:
            raise forms.ValidationError("Author name must be at least 2 characters long")
        return author