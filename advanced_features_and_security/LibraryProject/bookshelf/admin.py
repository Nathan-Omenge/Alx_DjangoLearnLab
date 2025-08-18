from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book


class CustomUserAdmin(UserAdmin):
    # show extra fields on the change form
    fieldsets = UserAdmin.fieldsets + (
        ("Profile", {"fields": ("date_of_birth", "profile_photo")}),
    )
    # show extra fields on the add form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Profile", {"fields": ("date_of_birth", "profile_photo")}),
    )
    # columns in the changelist
    list_display = ("username", "email", "is_staff", "date_of_birth")



admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)
    ordering = ("title",)