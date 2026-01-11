# Django CRUD Operations - Bookshelf App

## 1. Create
**Command:**
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

**Output:**
# <Book: 1984>

---

## 2. Retrieve
**Command:**
>>> book = Book.objects.get(title="1984")
>>> print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

**Output:**
# Title: 1984, Author: George Orwell, Year: 1949

---

## 3. Update
**Command:**
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book.title)

**Output:**
# Nineteen Eighty-Four

---

## 4. Delete
**Command:**
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
>>> Book.objects.all()

**Output:**
# (1, {'bookshelf.Book': 1})
# <QuerySet []>