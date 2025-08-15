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

**Output**
'Nineteen Eighty-Four'