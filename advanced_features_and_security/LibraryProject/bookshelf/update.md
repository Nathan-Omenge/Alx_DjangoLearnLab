---

#### 3. **update.md**
```markdown
# Update

**Command:**
```python
from bookshelf.models import Book
b = Book.objects.get(id=1)
b.title = "Nineteen Eighty-Four"
b.save()
Book.objects.get(id=1).title

from bookshelf.models import Book

# Get a book
book = Book.objects.get(id=1)

# Update the title
book.title = "Updated Book Title"
book.save()

**Output**
'Nineteen Eighty-Four'