from django.db import models


class Author(models.Model):
    """
    Model representing a book author.
    
    Attributes:
        name (CharField): The author's full name with a maximum length of 100 characters.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a book with its basic information and relationship to an author.
    
    Attributes:
        title (CharField): The book's title with a maximum length of 200 characters.
        publication_year (IntegerField): The year the book was published.
        author (ForeignKey): Foreign key linking to the Author model, establishing a 
                             one-to-many relationship from Author to Books. Uses CASCADE 
                             deletion to remove books when an author is deleted.
    
    The related_name='books' allows reverse access from Author instances to their books.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
