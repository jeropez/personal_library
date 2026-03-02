from .models import Book, Author, Genre
from .storage import Storage
from typing import List, Optional
from my_app import storage
from .exceptions import AuthorAlreadyExistsError, AuthorNotFoundError, GenreNotFoundError, BookNotFoundError, BookAlreadyExistsError,  GenreAlreadyExistsError, InvalidScoreError, PagesReadExceedsTotalError

class LibroService:
    """ Manages the core business logic for handling books, authors, and genres in the application.
    """
    def __init__(self, storage: Storage):
        self.storage = storage

    def add_book(self, libro: Book) -> None:
        libros = self.storage.load_books()

        if libro.id in [l.id for l in libros]:
            raise BookAlreadyExistsError(libro.id)

        libros.append(libro)
        self.storage.save_books(libros)

    def get_book(self, libro_id: int) -> Book:
        """ Gets a book by its ID.
        """
        libros = self.storage.load_books()
        for libro in libros:
            if libro.id == libro_id:
                return libro
        raise BookNotFoundError(libro_id)
        return libros           
    
    def delete_book(self, book_id: int) -> None:
        books = self.storage.load_books()

        book_to_delete = next((b for b in books if b.id == book_id), None)

        if not book_to_delete:
            raise BookNotFoundError(book_id)

        books.remove(book_to_delete)
        self.storage.save_books(books)

    def add_author(self, author: Author) -> None:
        autores = self.storage.load_authors()

        if any(a.id == author.id for a in autores):
            raise AuthorAlreadyExistsError(author.id)

        autores.append(author)
        self.storage.save_authors(autores)

    def get_author(self, author_id: int) -> Author:
        """ Gets an author by its ID.
        """
        autores = self.storage.load_authors()
        for autor in autores:
            if autor.id == author_id:
                return autor
        raise AuthorNotFoundError(author_id)

    def add_genre(self, genero: Genre) -> None:
        generos = self.storage.load_genres()

        if any(g.id == genero.id for g in generos):
            raise GenreAlreadyExistsError(genero.id)

        generos.append(genero)
        self.storage.save_genres(generos)

    def get_genre(self, genre_id: int) -> Genre:
        """ Gets a genre by its ID.
        """
        generos = self.storage.load_genres()
        for genero in generos:
            if genero.id == genre_id:
                return genero
        raise GenreNotFoundError(genre_id)
    
    def update_pages_read(self, libro_id: int, pages_read: int) -> None:
        libros = self.storage.load_books()
        for libro in libros:
            if libro.id == libro_id:
                if pages_read > libro.total_pages:
                    raise PagesReadExceedsTotalError(pages_read, libro.total_pages)

                libro.pages_read = pages_read
                self.storage.save_books(libros)
                return

        raise BookNotFoundError(libro_id)
    
    def rate_book(self, libro_id: int, score: int) -> None:
        if score < 1 or score > 5:
            raise InvalidScoreError(score)

        libros = self.storage.load_books()
        for libro in libros:
            if libro.id == libro_id:
                libro.score = score
                self.storage.save_books(libros)
                return

        raise BookNotFoundError(libro_id)
            
    def review_book(self, libro_id: int, review: str) -> None:
        """ Updates the review for a book.
        """
        libros = self.storage.load_books()
        for libro in libros:
            if libro.id == libro_id:
                libro.review = review
                self.storage.save_books(libros)
                return
        raise BookNotFoundError(libro_id)
    
    def list_authors_books(self, author_id: int) -> List[Book]:
        """ Lists all books by a specific author.
        """
        libros = self.storage.load_books()
        return [libro for libro in libros if libro.author_id == author_id]
        if not libros:
            raise AuthorNotFoundError(author_id)
    
    def list_genre_books(self, genre_id: int) -> List[Book]:
        """ Lists all books in a specific genre.
        """
        libros = self.storage.load_books()
        return [libro for libro in libros if libro.genre_id == genre_id]
        if not libros:
            raise GenreNotFoundError(genre_id)
