from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # columns shown on the list page
    list_display = ("id", "title", "author", "publication_year")

    # text search box (upper-right)
    search_fields = ("title", "author")

    # right-side filters
    list_filter = ("publication_year",)

    # optional: default ordering
    ordering = ("title",)
