# advanced_features_and_security/LibraryProject/bookshelf/admin.py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display  = ("id", "title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter   = ("publication_year",)
    ordering      = ("title",)