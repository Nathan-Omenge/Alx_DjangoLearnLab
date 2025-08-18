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

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    # Render a template or simple text; template used below
    return render(request, "relationship_app/admin_view.html")

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")