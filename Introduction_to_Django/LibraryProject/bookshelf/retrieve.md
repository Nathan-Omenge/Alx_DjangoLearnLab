---

#### 2. **retrieve.md**
```markdown
# Retrieve

**Command:**
```python
from bookshelf.models import Book
b = Book.objects.get(id=1)
(b.id, b.title, b.author, b.publication_year)

**Output**
(1, '1984', 'George Orwell', 1949)