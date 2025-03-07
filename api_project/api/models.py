from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    publication_year = models.DateField()