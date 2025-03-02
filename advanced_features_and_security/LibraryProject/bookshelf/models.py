from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=0)

    class Meta:
        permissions = [
            ("can_view", "Can view a book"),
            ("can_create", "Can create a book"),
            ("can_edit", "Can edit an existing book"),
            ("can_delete", "Can delete a book"),
        ]

    def __str__(self):
        return self.title, self.author, self.publication_year
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    username = None
    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = [] 

    objects = CustomUserManager()

    def __str__(self):
        return self.email