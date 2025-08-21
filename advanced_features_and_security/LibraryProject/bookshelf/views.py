# advanced_features_and_security/LibraryProject/bookshelf/views.py
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render  
from .models import Book      
From .forms import ExampleForm

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

@permission_required('bookshelf.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required("bookshelf.view_book", raise_exception=True)
def book_search(request):
    results = None
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data["q"]
            if q:
                results = Book.objects.filter(title__icontains=q)
            else:
                results = Book.objects.none()
    else:
        form = SearchForm()

    return render(
        request,
        "bookshelf/form_example.html",
        {"form": form, "results": results},
    )


def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Handle the data in form.cleaned_data as required
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            print(f"Received: {title} - {description}")
            # You can save to database or perform other actions here
    else:
        form = ExampleForm()

    return render(request, 'form_example.html', {'form': form})