from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Book, Library

# Function-based view: list all books
def list_books(request):
    books = Book.objects.select_related("author").all()
    # if you want plain text output (works without templates):
    # lines = [f"{b.title} by {b.author.name}" for b in books]
    # return HttpResponse("\n".join(lines), content_type="text/plain")
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based detail view for a Library (shows its books)
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"   # in template: {{ library }}

    # (Optional) ensure books are prefetched for efficiency
    def get_queryset(self):
        return Library.objects.prefetch_related("books__author")