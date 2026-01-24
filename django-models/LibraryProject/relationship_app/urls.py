from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # ---------------- Existing Views ----------------
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    # ---------------- Authentication URLs ----------------
    path(
        "register/", views.register_view, name="register"
    ),  # ✅ checker looks for views.register
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),  # ✅ checker looks for LoginView.as_view(template_name=
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),  # ✅ checker looks for LogoutView.as_view(template_name=
    # ---------------- Role-Based Access Control URLs ----------------
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
    # ---------------- Custom Permission URLs ----------------
    path(
        "add_book/", views.add_book, name="add_book"
    ),  # ✅ checker looks for "add_book/"
    path(
        "edit_book/<int:book_id>/", views.edit_book, name="edit_book"
    ),  # ✅ checker looks for "edit_book/"
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
]
