# Advanced API Project - Django REST Framework

This project demonstrates building custom views and generic views in Django REST Framework with advanced features including filtering, searching, ordering, and permission-based access control.

## Features

### Models
- **Author**: Represents book authors with name field
- **Book**: Represents books with title, publication_year, and foreign key to Author
- One-to-many relationship: Author → Books

### API Endpoints

#### Book List View
- **Endpoint**: `GET /api/books/`
- **Description**: Retrieve all books with advanced querying capabilities
- **Permissions**: Read-only access for all users (authenticated and unauthenticated)
- **Features**:
  - **Filtering**: Filter by title, author ID, or publication_year
  - **Search**: Search across book titles and author names
  - **Ordering**: Order by title, publication_year, or author name
  - **Default ordering**: Books ordered alphabetically by title

**Query Parameters**:
```
GET /api/books/?title=Harry                    # Filter by title containing "Harry"
GET /api/books/?author=1                       # Filter by author ID
GET /api/books/?publication_year=1997          # Filter by publication year
GET /api/books/?search=Potter                  # Search in titles and author names
GET /api/books/?ordering=publication_year      # Order by publication year (ascending)
GET /api/books/?ordering=-publication_year     # Order by publication year (descending)
```

#### Book Detail View
- **Endpoint**: `GET /api/books/{id}/`
- **Description**: Retrieve a single book by its ID
- **Permissions**: Read-only access for all users

#### Book Create View
- **Endpoint**: `POST /api/books/create/`
- **Description**: Create a new book
- **Permissions**: Authenticated users only
- **Validation**: 
  - Custom validation ensures publication_year is not in the future
  - All Book model fields are validated through BookSerializer
- **Response Format**:
  ```json
  {
    "message": "Book created successfully",
    "data": {
      "id": 1,
      "title": "New Book",
      "publication_year": 2020,
      "author": 1
    }
  }
  ```

#### Book Update View
- **Endpoint**: `PUT /api/books/{id}/update/` or `PATCH /api/books/{id}/update/`
- **Description**: Update an existing book (full or partial update)
- **Permissions**: Authenticated users only
- **Methods**:
  - **PUT**: Full update (all fields required)
  - **PATCH**: Partial update (only specified fields updated)
- **Response Format**:
  ```json
  {
    "message": "Book updated successfully",
    "data": {
      "id": 1,
      "title": "Updated Book",
      "publication_year": 2021,
      "author": 1
    }
  }
  ```

#### Book Delete View
- **Endpoint**: `DELETE /api/books/{id}/delete/`
- **Description**: Delete an existing book
- **Permissions**: Authenticated users only

## Custom Serializers

### BookSerializer
- **Purpose**: Handles serialization and validation for Book model
- **Custom Validation**: 
  - `validate_publication_year()`: Ensures publication year is not in the future
- **Fields**: All Book model fields (id, title, publication_year, author)

### AuthorSerializer
- **Purpose**: Handles serialization for Author model with nested book relationships
- **Features**:
  - Includes nested BookSerializer for related books
  - Dynamic serialization of all books by an author
  - Read-only books field (books cannot be modified through this serializer)
- **Fields**: id, name, books (nested)

## Permissions System

The API implements role-based access control:

### Read Operations (GET)
- **BookListView**: `IsAuthenticatedOrReadOnly` - Accessible to all users
- **BookDetailView**: `IsAuthenticatedOrReadOnly` - Accessible to all users

### Write Operations (POST, PUT, PATCH, DELETE)
- **BookCreateView**: `IsAuthenticated` - Authenticated users only
- **BookUpdateView**: `IsAuthenticated` - Authenticated users only  
- **BookDeleteView**: `IsAuthenticated` - Authenticated users only

## View Customizations

### Enhanced Response Handling
Both CreateView and UpdateView provide custom response formats with:
- Success/error messages
- Detailed error information for debugging
- Consistent response structure

### Advanced Filtering and Search
BookListView includes comprehensive querying capabilities:
- **DjangoFilterBackend**: Field-based filtering
- **SearchFilter**: Full-text search across multiple fields
- **OrderingFilter**: Flexible result ordering

### Custom Business Logic
- **perform_create()**: Extensible method for additional create logic
- **perform_update()**: Extensible method for additional update logic
- Custom validation integration with DRF serializers

## Installation and Setup

1. Install required dependencies:
   ```bash
   pip install django djangorestframework django-filter
   ```

2. Add to INSTALLED_APPS in settings.py:
   ```python
   INSTALLED_APPS = [
       # ... other apps
       'rest_framework',
       'django_filters',
       'api',
   ]
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Testing the API

### Using curl

1. **List all books**:
   ```bash
   curl -X GET http://127.0.0.1:8000/api/books/
   ```

2. **Get book details**:
   ```bash
   curl -X GET http://127.0.0.1:8000/api/books/1/
   ```

3. **Search books** (no authentication required):
   ```bash
   curl -X GET "http://127.0.0.1:8000/api/books/?search=Potter"
   ```

4. **Create a book** (requires authentication):
   ```bash
   curl -X POST http://127.0.0.1:8000/api/books/create/ \
        -H "Content-Type: application/json" \
        -H "Authorization: Token your_token_here" \
        -d '{"title": "New Book", "publication_year": 2020, "author": 1}'
   ```

### Using Django Admin or Shell

Create test data and users through Django admin interface or shell for comprehensive testing of authenticated endpoints.

## Advanced Query Features

### Filtering, Searching, and Ordering Implementation

The BookListView implements comprehensive filtering, searching, and ordering capabilities using Django REST Framework's built-in filter backends.

#### Filtering with DjangoFilterBackend

Filter books by exact matches on specific fields:

```bash
# Filter by exact title match
curl -X GET "http://127.0.0.1:8000/api/books/?title=Harry Potter and the Sorcerers Stone"

# Filter by author ID
curl -X GET "http://127.0.0.1:8000/api/books/?author=1"

# Filter by publication year
curl -X GET "http://127.0.0.1:8000/api/books/?publication_year=1997"

# Combine multiple filters
curl -X GET "http://127.0.0.1:8000/api/books/?author=1&publication_year=1997"
```

#### Search Functionality with SearchFilter

Perform text searches across title and author name fields:

```bash
# Search for books containing "Potter" in title or author name
curl -X GET "http://127.0.0.1:8000/api/books/?search=Potter"

# Search for books containing "Harry" in title or author name
curl -X GET "http://127.0.0.1:8000/api/books/?search=Harry"

# Search for author names
curl -X GET "http://127.0.0.1:8000/api/books/?search=Rowling"
```

#### Ordering with OrderingFilter

Sort results by any field in ascending or descending order:

```bash
# Order by title (ascending - default)
curl -X GET "http://127.0.0.1:8000/api/books/?ordering=title"

# Order by title (descending)
curl -X GET "http://127.0.0.1:8000/api/books/?ordering=-title"

# Order by publication year (ascending)
curl -X GET "http://127.0.0.1:8000/api/books/?ordering=publication_year"

# Order by publication year (descending)
curl -X GET "http://127.0.0.1:8000/api/books/?ordering=-publication_year"

# Order by author name
curl -X GET "http://127.0.0.1:8000/api/books/?ordering=author__name"

# Multiple ordering criteria
curl -X GET "http://127.0.0.1:8000/api/books/?ordering=author__name,publication_year"
```

#### Combined Query Examples

Combine filtering, searching, and ordering in a single request:

```bash
# Search for "Potter" books and order by publication year
curl -X GET "http://127.0.0.1:8000/api/books/?search=Potter&ordering=publication_year"

# Filter by author and order by title descending
curl -X GET "http://127.0.0.1:8000/api/books/?author=1&ordering=-title"

# Search, filter by year, and order by title
curl -X GET "http://127.0.0.1:8000/api/books/?search=Harry&publication_year=1997&ordering=title"
```

#### Implementation Details

The filtering, searching, and ordering functionality is implemented in the BookListView with the following configuration:

```python
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Filtering configuration
    filterset_fields = ['title', 'author', 'publication_year']
    
    # Search configuration
    search_fields = ['title', 'author__name']
    
    # Ordering configuration
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['title']  # Default ordering
```

**Filter Backends Used:**
- **DjangoFilterBackend**: Enables exact-match filtering on specified fields
- **SearchFilter**: Enables text-based searching across specified fields
- **OrderingFilter**: Enables sorting by specified fields in ascending/descending order

**Default Behavior:**
- Results are ordered by title (ascending) by default
- All users can use filtering, searching, and ordering (no authentication required for read operations)
- Search is case-insensitive and supports partial matches
- Filtering requires exact matches for the specified field values

## Testing

### Running Tests

Execute the comprehensive unit test suite:

```bash
python manage.py test api
```

### Test Coverage

The test suite includes:

- **CRUD Operations**: Create, Read operations for Books
- **Authentication & Permissions**: Authenticated vs unauthenticated access
- **Custom Validation**: Publication year validation
- **Filtering**: Filter by title, author, publication year
- **Search**: Text search across titles and author names
- **Ordering**: Sort by multiple fields in both directions
- **Serialization**: Author model with nested books

### Test Structure

Tests are located in `/api/test_views.py` and include:
- `BookAPITestCase`: Comprehensive API endpoint testing
- `AuthorAPITestCase`: Author serialization with nested books
- `BookSerializerTestCase`: Custom serializer validation

## Architecture Notes

- **Generic Views**: Leverages DRF's built-in generic views for standard CRUD operations
- **Custom Mixins**: Views can be easily extended with additional functionality
- **Serializer Integration**: Seamless integration between models, serializers, and views
- **Permission Classes**: Flexible permission system using DRF's built-in classes
- **Filter Integration**: Advanced querying capabilities through django-filter integration
- **Test Coverage**: Comprehensive unit tests ensure API reliability and correctness

This implementation demonstrates best practices for building scalable, maintainable REST APIs with Django REST Framework.