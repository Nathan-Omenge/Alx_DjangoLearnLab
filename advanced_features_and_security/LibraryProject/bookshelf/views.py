# advanced_features_and_security/LibraryProject/bookshelf/views.py
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return HttpResponse("Create book (requires bookshelf.can_create)")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    return HttpResponse(f"Edit book {pk} (requires bookshelf.can_edit)")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    return HttpResponse(f"Delete book {pk} (requires bookshelf.can_delete)")

@permission_required('bookshelf.can_view', raise_exception=True)
def list_books_secure(request):
    return HttpResponse("List books (requires bookshelf.can_view)")