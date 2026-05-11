from personal_library.models.book import Book
from personal_library.models.author import Author
from personal_library.models.genre import Genre

from personal_library.exceptions import (
    BookAlreadyExistsError,
    BookNotFoundError,
    AuthorAlreadyExistsError,
    AuthorNotFoundError,
    GenreAlreadyExistsError,
    GenreNotFoundError,
    InvalidScoreError,
    PagesReadExceedsTotalError,
)


class BookService:
    """Service layer for managing books, authors, and genres."""

    def __init__(self, storage):
        self.storage = storage

    # ---------------- BOOKS ----------------

    def add_book(self, book: Book) -> None:
        books = self.storage.load_books()

        if any(b.id == book.id for b in books):
            raise BookAlreadyExistsError(book.id)

        books.append(book)
        self.storage.save_books(books)

    def get_book(self, book_id: int) -> Book:
        books = self.storage.load_books()

        for book in books:
            if book.id == book_id:
                return book

        raise BookNotFoundError(book_id)

    def delete_book(self, book_id: int) -> None:
        books = self.storage.load_books()

        filtered_books = [book for book in books if book.id != book_id]

        if len(filtered_books) == len(books):
            raise BookNotFoundError(book_id)

        self.storage.save_books(filtered_books)

    def all_books(self) -> list[Book]:
        return self.storage.load_books()

    def update_pages_read(self, book_id: int, pages: int) -> None:
        books = self.storage.load_books()

        for book in books:
            if book.id == book_id:
                if pages > book.total_pages:
                    raise PagesReadExceedsTotalError(
                        pages,
                        book.total_pages
                    )

                book.read_pages = pages
                self.storage.save_books(books)
                return

        raise BookNotFoundError(book_id)

    def rate_book(self, book_id: int, score: int) -> None:
        if score < 1 or score > 5:
            raise InvalidScoreError(score)

        books = self.storage.load_books()

        for book in books:
            if book.id == book_id:
                book.score = score
                self.storage.save_books(books)
                return

        raise BookNotFoundError(book_id)

    def review_book(self, book_id: int, review: str) -> None:
        books = self.storage.load_books()

        for book in books:
            if book.id == book_id:
                book.review = review
                self.storage.save_books(books)
                return

        raise BookNotFoundError(book_id)

    def list_authors_books(self, author_id: int) -> list[Book]:
        books = self.storage.load_books()

        author_books = [
            book for book in books
            if book.author_id == author_id
        ]

        if not author_books:
            raise AuthorNotFoundError(author_id)

        return author_books

    def list_genre_books(self, genre_id: int) -> list[Book]:
        books = self.storage.load_books()

        genre_books = [
            book for book in books
            if book.genre_id == genre_id
        ]

        if not genre_books:
            raise GenreNotFoundError(genre_id)

        return genre_books

    def show_book_details(self, book_id: int) -> Book:
        return self.get_book(book_id)

    # ---------------- AUTHORS ----------------

    def add_author(self, author: Author) -> None:
        authors = self.storage.load_authors()

        if any(a.id == author.id for a in authors):
            raise AuthorAlreadyExistsError(author.id)

        authors.append(author)
        self.storage.save_authors(authors)

    def get_author(self, author_id: int) -> Author:
        authors = self.storage.load_authors()

        for author in authors:
            if author.id == author_id:
                return author

        raise AuthorNotFoundError(author_id)

    def all_authors(self) -> list[Author]:
        return self.storage.load_authors()

    # ---------------- GENRES ----------------

    def add_genre(self, genre: Genre) -> None:
        genres = self.storage.load_genres()

        if any(g.id == genre.id for g in genres):
            raise GenreAlreadyExistsError(genre.id)

        genres.append(genre)
        self.storage.save_genres(genres)

    def get_genre(self, genre_id: int) -> Genre:
        genres = self.storage.load_genres()

        for genre in genres:
            if genre.id == genre_id:
                return genre

        raise GenreNotFoundError(genre_id)

    def all_genres(self) -> list[Genre]:
        return self.storage.load_genres()