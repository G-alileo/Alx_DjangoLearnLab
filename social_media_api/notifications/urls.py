from django.urls import path
from .views import user_notifications

urlpatterns = [
    path('', user_notifications, name='user_notifications'),
]

