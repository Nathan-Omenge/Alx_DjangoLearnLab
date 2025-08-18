# advanced_features_and_security/LibraryProject/bookshelf/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# -----------------------------
# Book model (unchanged)
# -----------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.publication_year})"


# -----------------------------
# Custom user manager
# -----------------------------
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        Create and save a regular user with the given username, email and password.
        Email is required here for clarity (adjust if you want it optional).
        """
        if not username:
            raise ValueError("The username must be set")
        if not email:
            raise ValueError("The email must be set")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        Create and save a superuser with the given username, email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email=email, password=password, **extra_fields)


# -----------------------------
# Custom user model
# -----------------------------
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profiles/", null=True, blank=True)

    # Tell Django to use our custom manager
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.username