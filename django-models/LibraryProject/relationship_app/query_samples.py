from relationship_app.models import Author, Library


def run_queries():
    # Query all books by a specific author
    author = Author.objects.get(name="J.K. Rowling")
    print("Books by J.K. Rowling:")
    for book in author.books.all():
        print("-", book.title)

    # List all books in a library
    library = Library.objects.get(name="Central Library")
    print("\nBooks in Central Library:")
    for book in library.books.all():
        print("-", book.title)

    # Retrieve the librarian for a library
    print("\nLibrarian of Central Library:", library.librarian.name)
