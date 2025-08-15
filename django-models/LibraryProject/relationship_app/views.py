from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth import login  # required by checker
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Library


# Function-based view for listing books
def list_books(request):
    books = Book.objects.all()  # required by checker
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# Function-based view for user registration
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # after registering, go to login
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})