from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm, ExampleForm


# ✅ Secure search using ORM (no raw SQL)
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    query = request.GET.get("q", "")
    books = Book.objects.filter(title__icontains=query)  # ORM prevents SQL injection
    return render(request, "bookshelf/book_list.html", {"books": books})


# ✅ Secure book creation using BookForm
@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():  # validates and sanitizes input
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form})


# ✅ Secure book editing
@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/form_example.html", {"form": form})


# ✅ Secure book deletion
@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/confirm_delete.html", {"book": book})


# ✅ ExampleForm usage (demonstrates CSRF + validation)
def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Safe handling of validated data
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            # Normally you’d save or process this data securely
            return render(request, "bookshelf/form_success.html", {"name": name})
    else:
        form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form": form})
