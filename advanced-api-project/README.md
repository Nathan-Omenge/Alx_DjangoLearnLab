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

## Architecture Notes

- **Generic Views**: Leverages DRF's built-in generic views for standard CRUD operations
- **Custom Mixins**: Views can be easily extended with additional functionality
- **Serializer Integration**: Seamless integration between models, serializers, and views
- **Permission Classes**: Flexible permission system using DRF's built-in classes
- **Filter Integration**: Advanced querying capabilities through django-filter integration

This implementation demonstrates best practices for building scalable, maintainable REST APIs with Django REST Framework.