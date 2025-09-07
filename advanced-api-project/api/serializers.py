from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model that handles serialization and validation of book data.
    
    This serializer includes all fields from the Book model and implements custom validation
    to ensure the publication_year is not in the future.
    
    Attributes:
        Meta.model (Book): The model this serializer is based on.
        Meta.fields (str): Includes all fields from the Book model.
    """
    
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom validation method for the publication_year field.
        
        Ensures that the publication year is not in the future by comparing
        it with the current year.
        
        Args:
            value (int): The publication year to validate.
            
        Returns:
            int: The validated publication year.
            
        Raises:
            serializers.ValidationError: If the publication year is in the future.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model that includes nested serialization of related books.
    
    This serializer demonstrates a one-to-many relationship by including all books
    written by the author through the nested BookSerializer. The books field is
    read-only, meaning it's included in serialization but not used during
    deserialization (creation/updates).
    
    Attributes:
        books (BookSerializer): Nested serializer for related Book instances.
                                Uses many=True for multiple books and read_only=True
                                to prevent modification through this serializer.
        Meta.model (Author): The model this serializer is based on.
        Meta.fields (list): Explicitly lists the fields to include in serialization.
    
    The relationship between Author and Book is handled through the 'books' related_name
    defined in the Book model's ForeignKey field, allowing dynamic serialization of
    all books associated with an author.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']