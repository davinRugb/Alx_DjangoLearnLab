# Integrating the Book Model with Django Admin

## Step 1: Register the Book Model
- Open `bookshelf/admin.py`.
- Register the `Book` model using the following code:
  ```python
  from django.contrib import admin
  from .models import Book

  @admin.register(Book)
  class BookAdmin(admin.ModelAdmin):
      list_display = ('title', 'author', 'publication_year')
      list_filter = ('author', 'publication_year')
      search_fields = ('title', 'author')
