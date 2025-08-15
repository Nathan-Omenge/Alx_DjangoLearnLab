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

**Output**
(1, [])