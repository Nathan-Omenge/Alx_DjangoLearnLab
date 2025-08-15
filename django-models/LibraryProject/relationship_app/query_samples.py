from relationship_app.models import Author, Book, Library, Librarian

# 1) All books by a specific author
def books_by_author(author_name: str):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# 2) All books in a library
def books_in_library(library_name: str):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3) The librarian for a library
def librarian_for_library(library_name: str):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)