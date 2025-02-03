# addition_backend/api/urls.py

from django.urls import path
from .views import add_numbers  # Ensure this import is correct

urlpatterns = [
    path('add/', add_numbers, name="add-numbers"),
]
