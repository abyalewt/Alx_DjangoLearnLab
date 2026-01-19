from relationship_app.models import Author, Library


def run_queries():
    # Query all books by a specific author
    author_name = "J.K. Rowling"
    author = Author.objects.get(name=author_name)
    print(f"Books by {author_name}:")
    for book in author.books.all():
        print("-", book.title)

    # List all books in a library
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    print(f"\nBooks in {library_name}:")
    for book in library.books.all():
        print("-", book.title)

    # Retrieve the librarian for a library
    print(f"\nLibrarian of {library_name}: {library.librarian.name}")
