from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as django_filters
import django_filters
from .models import Book
from .serializers import BookSerializer


class BookFilter(django_filters.FilterSet):
    """
    Custom filter class for Book model.
    
    Provides filtering capabilities for title, author, and publication_year fields.
    """
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.NumberFilter()
    publication_year = django_filters.NumberFilter()
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class BookListView(generics.ListAPIView):
    """
    API view for retrieving all books with filtering, searching, and ordering capabilities.
    
    This view provides read-only access to all Book instances in the database with
    advanced querying features. It uses the BookSerializer to format the response data
    and allows both authenticated and unauthenticated users to view the book list.
    
    Features:
    - Filter by title, author, or publication_year
    - Search across title and author name
    - Order by title, publication_year, or author name
    
    Endpoint: GET /books/
    Permissions: Read-only access for all users
    Query Parameters:
        - title: Filter by book title
        - author: Filter by author ID
        - publication_year: Filter by publication year
        - search: Search in title and author name
        - ordering: Order by field (prefix with '-' for descending)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['title']  # Default ordering


class BookDetailView(generics.RetrieveAPIView):
    """
    API view for retrieving a single book by ID.
    
    This view provides read-only access to a specific Book instance identified
    by its primary key. It uses the BookSerializer to format the response data
    and allows both authenticated and unauthenticated users to view book details.
    
    Endpoint: GET /books/{id}/
    Permissions: Read-only access for all users
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    API view for creating a new book with enhanced validation and custom responses.
    
    This view allows authenticated users to create new Book instances.
    It uses the BookSerializer for data validation and serialization,
    including custom validation for publication_year. Provides detailed
    success and error responses.
    
    Endpoint: POST /books/create/
    Permissions: Authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom create method to handle additional logic during book creation.
        
        This method can be extended to add custom behavior such as setting
        additional fields, logging, or sending notifications.
        """
        serializer.save()

    def create(self, request, *args, **kwargs):
        """
        Custom create method with enhanced response handling.
        
        Provides detailed success messages and proper error handling
        for better API user experience.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'message': 'Book created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({
                'message': 'Failed to create book',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class BookUpdateView(generics.UpdateAPIView):
    """
    API view for updating an existing book with enhanced validation and responses.
    
    This view allows authenticated users to update existing Book instances
    using PUT (full update) or PATCH (partial update) methods.
    It uses the BookSerializer for data validation and serialization with
    enhanced response handling.
    
    Endpoint: PUT/PATCH /books/{id}/update/
    Permissions: Authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom update method to handle additional logic during book updates.
        
        This method can be extended to add custom behavior such as logging
        changes, validating business rules, or sending notifications.
        """
        serializer.save()

    def update(self, request, *args, **kwargs):
        """
        Custom update method with enhanced response handling.
        
        Provides detailed success messages and proper error handling
        for both full (PUT) and partial (PATCH) updates.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({
                'message': 'Book updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': 'Failed to update book',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        """
        Handle PATCH requests for partial updates.
        """
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class BookDeleteView(generics.DestroyAPIView):
    """
    API view for deleting an existing book.
    
    This view allows authenticated users to delete existing Book instances.
    Once deleted, the book will be permanently removed from the database.
    
    Endpoint: DELETE /books/{id}/delete/
    Permissions: Authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
