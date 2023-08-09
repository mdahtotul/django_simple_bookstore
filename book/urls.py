from django.urls import path

from book.views import (
    BookDeleteView,
    BookDetailView,
    BookFormView,
    BookListView,
    BookUpdateView,
    HomeView,
)

# from book.views import store_book, home, show_books, edit_book, delete_book


"""
urlpatterns = [
    path("", home, name="home"),
    path("store-book/", store_book, name="store_book"),
    path("show-books/", show_books, name="show_books"),
    path("edit-book/<int:id>", edit_book, name="edit_book"),
    path("delete-book/<int:id>", delete_book, name="delete_book"),
]
"""

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("store-book/", BookFormView.as_view(), name="store_book"),
    path("show-books/", BookListView.as_view(), name="show_books"),
    path("show-books/<int:pk>", BookDetailView.as_view(), name="book_detail"),
    path("edit-book/<int:pk>", BookUpdateView.as_view(), name="edit_book"),
    path("delete-book/<int:pk>", BookDeleteView.as_view(), name="delete_book"),
]
