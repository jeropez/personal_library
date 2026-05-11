from personal_library.models import Book


class BookService:
    def __init__(self, storage):
        self.storage = storage

    def add_book(self, book: Book) -> None:
        """Adds a new book."""
        self.storage.add_book(book)

    def list_books(self) -> list[Book]:
        """Returns all books."""
        return self.storage.list_books()

    def delete_book(self, book_id: int) -> None:
        """Deletes a book."""
        self.storage.delete_book(book_id)