# advanced_features_and_security/LibraryProject/bookshelf/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_book, name='create_book'),
    path('<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('list/', views.list_books_secure, name='list_books_secure'),
    path('books/', views.book_list, name='book_list'),
    path("books/search/", views.book_search, name="book_search"),
]