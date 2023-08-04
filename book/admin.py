from django.contrib import admin

from book.models import BookStoreModel


# Register your models here.
@admin.register(BookStoreModel)
class BookStoreAdmin(admin.ModelAdmin):
    list_display = ["id", "book_name", "category"]
    readonly_fields = ["first_published", "last_published"]
    list_editable = ["book_name", "category"]
    list_per_page = 15
    ordering = ["book_name", "last_published"]
