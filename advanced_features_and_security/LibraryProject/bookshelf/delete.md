---

#### 4. **delete.md**
```markdown
# Delete

**Command:**
```python
from bookshelf.models import Book
b = Book.objects.get(id=1)
deleted, _ = b.delete()
deleted, list(Book.objects.values())

# Delete a Book

Run the following command to delete a book:

```bash
book.delete

**Output**
(1, [])