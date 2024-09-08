from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookViewSet

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve a single book by ID
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Add a new book
    path('books/update/', BookUpdateView.as_view(), name='book-update'),  # Update an existing book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete a book
]
  

# api/urls.py


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
