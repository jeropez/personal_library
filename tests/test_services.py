import pytest 
from my_app.services import LibroService
from unittest.mock import MagicMock
from my_app.models import (Book, 
                           Author, 
                           Genre)
from my_app.exceptions import (
    AuthorAlreadyExistsError, 
    AuthorNotFoundError, 
    GenreNotFoundError, 
    BookNotFoundError, 
    BookAlreadyExistsError,  
    GenreAlreadyExistsError, 
    InvalidScoreError, 
    PagesReadExceedsTotalError)

def test_add_and_get_book(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_books.return_value = []
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    book = Book(id=1, title="Test Book", author_id=1, publishing_year=2020, total_pages=300, pages_read=150, genre_id="Fiction", score=4, review="Great book!")
    service.add_book(book)

    mock_storage.save_books.assert_called_once_with([book])
    mock_storage.load_books.return_value = [book]
    retrieved_book = service.get_book(1)
    assert retrieved_book == book


def test_add_duplicate_book(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_books.return_value = []
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    book = Book(id=1, title="Test Book", author_id=1, publishing_year=2020, total_pages=300, pages_read=150, genre_id="Fiction", score=4, review="Great book!")
    service.add_book(book)

    with pytest.raises(BookAlreadyExistsError):
        service.add_book(book)

def test_get_nonexistent_book(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_books.return_value = []
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    with pytest.raises(BookNotFoundError):
        service.get_book(999)

def test_delete_book(libro_service):
    mock_storage = MagicMock()
    book = Book(id=1, title="Test Book", author_id=1, publishing_year=2020, total_pages=300, pages_read=150, genre_id="Fiction", score=4, review="Great book!")
    mock_storage.load_books.return_value = [book]
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    service.delete_book(1)

    mock_storage.save_books.assert_called_once_with([])
    with pytest.raises(BookNotFoundError):
        service.get_book(1)

def test_add_and_get_author(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_authors.return_value = []
    libro_service.storage = mock_storage
    service = LibroService(mock_storage)
    author = Author(id=1, name="Test Author")

    service.add_author(author)
    mock_storage.save_authors.assert_called_once_with([author])
    mock_storage.load_authors.return_value = [author]
    retrieved_author = service.get_author(1)
    assert retrieved_author == author

def test_add_duplicate_author(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_authors.return_value = []
    libro_service.storage = mock_storage
    service = LibroService(mock_storage)
    author = Author(id=1, name="Test Author")

    service.add_author(author)
    with pytest.raises(AuthorAlreadyExistsError):
        service.add_author(author)

def test_get_nonexistent_author(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_authors.return_value = []
    libro_service.storage = mock_storage
    service = LibroService(mock_storage)

    with pytest.raises(AuthorNotFoundError):
        service.get_author(999)

def test_add_and_get_genre(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_genres.return_value = []
    libro_service.storage = mock_storage
    service = LibroService(mock_storage)
    genre = Genre(id=1, name="Fiction")

    service.add_genre(genre)
    mock_storage.save_genres.assert_called_once_with([genre])
    mock_storage.load_genres.return_value = [genre]
    retrieved_genre = service.get_genre(1)
    assert retrieved_genre == genre

def test_add_duplicate_genre(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_genres.return_value = []
    libro_service.storage = mock_storage
    service = LibroService(mock_storage)
    genre = Genre(id=1, name="Fiction")

    service.add_genre(genre)
    with pytest.raises(GenreAlreadyExistsError):
        service.add_genre(genre)

def test_get_nonexistent_genre(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_genres.return_value = []
    libro_service.storage = mock_storage
    service = LibroService(mock_storage)

    with pytest.raises(GenreNotFoundError):
        service.get_genre(999)

def test_update_pages_read_exceeds_total(libro_service):
    mock_storage = MagicMock()
    book = Book(id=1, title="Test Book", author_id=1, publishing_year=2020, total_pages=300, pages_read=150, genre_id="Fiction", score=4, review="Great book!")
    mock_storage.load_books.return_value = [book]
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    with pytest.raises(PagesReadExceedsTotalError):
        service.update_pages_read(1, 350)

def test_rate_book_invalid_score(libro_service):
    mock_storage = MagicMock()
    book = Book(id=1, title="Test Book", author_id=1, publishing_year=2020, total_pages=300, pages_read=150, genre_id="Fiction", score=4, review="Great book!")
    mock_storage.load_books.return_value = [book]
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    with pytest.raises(InvalidScoreError):
        service.rate_book(1, 6)

def test_rate_book_nonexistent(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_books.return_value = []
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    with pytest.raises(BookNotFoundError):
        service.rate_book(999, 4)

def test_update_pages_read_nonexistent_book(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_books.return_value = []
    libro_service.storage = mock_storage
    service = LibroService(mock_storage)
    with pytest.raises(BookNotFoundError):
        service.update_pages_read(999, 100)

def test_delete_nonexistent_book(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_books.return_value = []
    libro_service.storage = mock_storage
    service = LibroService(mock_storage)
    with pytest.raises(BookNotFoundError):
        service.delete_book(999)
