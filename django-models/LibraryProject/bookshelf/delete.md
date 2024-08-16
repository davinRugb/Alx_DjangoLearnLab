"# LibraryProject" 
# Delete Operation
from bookshelf.models import Book
```python
retrieved_book.delete()
all_books = Book.objects.all()
print(list(all_books))
# Expected Output: Book instance deleted; no books in the database.

