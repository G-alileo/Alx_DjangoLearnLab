from django.urls import path
from .views import book_create, book_edit, book_delete, book_list, form_example


urlpatterns = [
    path('list/', book_list, name='book_list'),
    path('create/', book_create, name='book_create'),
    path('edit/<int:book_id>/', book_edit, name='book_edit'), 
    path('delete/<int:book_id>/', book_delete, name='book_delete'),
    path('example-form/', form_example, name='form_example'),  
]
