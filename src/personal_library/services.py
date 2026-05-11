from .models import Book, Author, Genre
from .storage import Storage
from typing import List
from .exceptions import AuthorAlreadyExistsError, AuthorNotFoundError, GenreNotFoundError, BookNotFoundError, BookAlreadyExistsError,  GenreAlreadyExistsError, InvalidInputError, InvalidScoreError, PagesReadExceedsTotalError

class LibroService:
    """ Manages the core business logic for handling books, authors, and genres in the application.
    """
    def __init__(self, storage: Storage):
        self.storage = storage

    def add_book(self, libro: Book) -> None:
        libros = self.storage.load_books()

        if libro.id in [book.id for book in libros]:
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

    def get_genre(self, genre_id: int | str) -> Genre:
        """Gets a genre by its ID or name."""
        genres = self.storage.load_genres()

        for genre in genres:
            if isinstance(genre_id, int) and genre.id == genre_id:
                return genre
            if isinstance(genre_id, str) and genre.name == genre_id:
                return genre

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
    
    def list_authors_books(self, author_id: int) -> list[Book]:
        books = self.storage.load_books()

        filtered = [book for book in books if book.author_id == author_id]

        if not filtered:
            raise AuthorNotFoundError(author_id)

        return filtered   
        
    def list_genre_books(self, genre_id: str) -> list[Book]:
        books = self.storage.load_books()

        filtered = [book for book in books if book.genre_id == genre_id]

        if not filtered:
            raise GenreNotFoundError(genre_id)

        return filtered
    
    def all_books(self) -> List[Book]:
        """ Returns a list of all books in the storage.
        """
        return self.storage.load_books()
    
    def all_authors(self) -> List[Author]:
        """ Returns a list of all authors in the storage.
        """
        return self.storage.load_authors()
    
    def all_genres(self) -> List[Genre]:
        """ Returns a list of all genres in the storage.
        """
        return self.storage.load_genres()
    
    def show_book_details(self, libro_id: int) -> Book:
        """ Returns a book with its author and genre details.
        """
        libro = self.get_book(libro_id)
        libro.author = self.get_author(libro.author_id)
        libro.genre = self.get_genre(libro.genre_id)
        libro.total_pages = libro.total_pages
        libro.pages_read = libro.pages_read
        libro.score = libro.score
        libro.review = libro.review
        return libro

    def add_book_manual(
    self,
    title: str,
    author_id: int,
    publishing_year: int,
    total_pages: int,
    genre_id: str,
) -> None:

        books = self.storage.load_books()

        # Generar nuevo ID automático
        new_id = max((book.id for book in books), default=0) + 1

        # Validar que el autor exista
        authors = self.storage.load_authors()
        if not any(author.id == author_id for author in authors):
            raise AuthorNotFoundError(author_id)

        # Validar que el género exista (por nombre)
        genres = self.storage.load_genres()
        if not any(genre.name == genre_id for genre in genres):
            raise GenreNotFoundError(genre_id)

        # Validar páginas
        if total_pages <= 0:
            raise InvalidInputError("Total pages must be greater than 0.")

        # Crear libro
        new_book = Book(
            id=new_id,
            title=title,
            author_id=author_id,
            publishing_year=publishing_year,
            total_pages=total_pages,
            pages_read=0,
            genre_id=genre_id,
            score=None,
            review=None,
        )

        books.append(new_book)
        self.storage.save_books(books)
    
    def add_author_manual(self, name: str) -> None:
        authors = self.storage.load_authors()

        new_id = max((author.id for author in authors), default=0) + 1

        new_author = Author(id=new_id, name=name)

        if any(a.name == name for a in authors):
            raise AuthorAlreadyExistsError(name)

        authors.append(new_author)
        self.storage.save_authors(authors)
    
    def add_genre_manual(self, name: str) -> None:
        genres = self.storage.load_genres()

        new_id = max((genre.id for genre in genres if isinstance(genre.id, int)), default=0) + 1

        new_genre = Genre(id=new_id, name=name)

        if any(g.name == name for g in genres):
            raise GenreAlreadyExistsError(name)
    
        genres.append(new_genre)
        self.storage.save_genres(genres)
