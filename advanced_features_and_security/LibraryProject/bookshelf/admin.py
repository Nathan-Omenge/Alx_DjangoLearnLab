# advanced_features_and_security/LibraryProject/bookshelf/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # show extra profile fields on the user change page
    fieldsets = UserAdmin.fieldsets + (
        ("Profile", {"fields": ("date_of_birth", "profile_photo")}),
    )
    # show extra profile fields on the user add page
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Profile", {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = ("username", "email", "is_staff", "date_of_birth")
    search_fields = ("username", "email")

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display  = ("id", "title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter   = ("publication_year",)
    ordering      = ("title",)