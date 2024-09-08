from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from .forms import BookForm  # Assuming you've created a form for Book

# ListView: To retrieve all books
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'  # Template for listing books
    context_object_name = 'books'  # Name for the list of books in the template

# DetailView: To retrieve a single book by its ID
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'  # Template for displaying a single book
    context_object_name = 'book'  # Name for the book object in the template

# CreateView: To add a new book
class BookCreateView(CreateView):
    model = Book
    form_class = BookForm  # Form for creating a new book
    template_name = 'books/book_form.html'  # Template for the form
    success_url = reverse_lazy('book-list')  # Redirect to the book list after successful creation

# UpdateView: To modify an existing book
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm  # Form for updating a book
    template_name = 'books/book_form.html'  # Reusing the same form template as for creating
    success_url = reverse_lazy('book-list')  # Redirect to the book list after successful update

# DeleteView: To delete a book
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'  # Confirmation page template for deleting a book
    success_url = reverse_lazy('book-list')  # Redirect to the book list after successful deletion



