from django.urls import path
from . import views

urlpatterns = [
    # Book list view - GET /books/
    path('books/', views.BookListView.as_view(), name='book-list'),
    
    # Book detail view - GET /books/{id}/
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    
    # Book create view - POST /books/create/
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    
    # Book update view - PUT/PATCH /books/update/
    path('books/update/', views.BookUpdateView.as_view(), name='book-update'),
    
    # Book delete view - DELETE /books/delete/
    path('books/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]