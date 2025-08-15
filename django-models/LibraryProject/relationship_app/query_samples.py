from relationship_app.models import Author, Book, Library, Librarian

# 1) All books by a specific author
def books_by_author(author_name: str):
    return Book.objects.filter(author__name=author_name)

# 2) All books in a library
def books_in_library(library_name: str):
    return Library.objects.get(name=library_name).books.all()

# 3) The librarian for a library
def librarian_for_library(library_name: str):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)