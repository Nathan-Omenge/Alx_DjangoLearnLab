# CRUD Operations (Django Shell)

```python
# CREATE
from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
b.id
# Output:
1

# RETRIEVE
b = Book.objects.get(id=1)
(b.id, b.title, b.author, b.publication_year)
# Output:
(1, '1984', 'George Orwell', 1949)

# UPDATE
b = Book.objects.get(id=1)
b.title = "Nineteen Eighty-Four"
b.save()
Book.objects.get(id=1).title
# Output:
'Nineteen Eighty-Four'

# DELETE
b = Book.objects.get(id=1)
deleted, _ = b.delete()
deleted, list(Book.objects.values())
# Output:
(1, [])