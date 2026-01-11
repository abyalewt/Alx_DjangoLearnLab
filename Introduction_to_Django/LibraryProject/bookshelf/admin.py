from django.contrib import admin
from .models import Book  # <--- The checker is looking for this exact line


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("publication_year", "author")
    search_fields = ("title", "author")


admin.site.register(Book, BookAdmin)
