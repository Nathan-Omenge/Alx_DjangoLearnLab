from django.urls import path
from .views import list_books, LibraryDetailView   # 👈 explicit import

app_name = "relationship_app"

urlpatterns = [
    path("books/", list_books, name="list_books"),  # FBV
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  
]

from django.urls import path
from .views import (
    list_books, LibraryDetailView,  # existing
    UserLoginView, UserLogoutView, RegisterView  # new
)

app_name = "relationship_app"

urlpatterns = [
    # existing
    path("books/", list_books, name="list_books"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # auth
    path("login/",  UserLoginView.as_view(),  name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(),  name="register"),
]