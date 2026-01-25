from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]

    # Example of extra validation
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 2:
            raise forms.ValidationError("Title must be at least 2 characters long.")
        return title
