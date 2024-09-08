from django import forms
from .models import Book

# BookForm: A form for creating and updating Book instances
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields from the Book model
