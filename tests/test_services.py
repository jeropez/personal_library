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

def test_review_book_nonexistent(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_books.return_value = []
    libro_service.storage = mock_storage
    service = LibroService(mock_storage)
    with pytest.raises(BookNotFoundError):
        service.review_book(999, "This is a review.")

def test_list_authors_books(libro_service):
    mock_storage = MagicMock()
    book1 = Book(id=1, title="Book 1", author_id=1, publishing_year=2020, total_pages=300, pages_read=150, genre_id="Fiction", score=4, review="Great book!")
    book2 = Book(id=2, title="Book 2", author_id=1, publishing_year=2021, total_pages=250, pages_read=100, genre_id="Fiction", score=5, review="Excellent!")
    book3 = Book(id=3, title="Book 3", author_id=2, publishing_year=2019, total_pages=200, pages_read=50, genre_id="Non-Fiction", score=3, review="Good read.")
    mock_storage.load_books.return_value = [book1, book2, book3]
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    authors_books = service.list_authors_books(1)
    assert authors_books == [book1, book2]

def test_list_genre_books(libro_service):
    mock_storage = MagicMock()
    book1 = Book(id=1, title="Book 1", author_id=1, publishing_year=2020, total_pages=300, pages_read=150, genre_id="Fiction", score=4, review="Great book!")
    book2 = Book(id=2, title="Book 2", author_id=1, publishing_year=2021, total_pages=250, pages_read=100, genre_id="Fiction", score=5, review="Excellent!")
    book3 = Book(id=3, title="Book 3", author_id=2, publishing_year=2019, total_pages=200, pages_read=50, genre_id="Non-Fiction", score=3, review="Good read.")
    mock_storage.load_books.return_value = [book1, book2, book3]
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    genre_books = service.list_genre_books("Fiction")
    assert genre_books == [book1, book2]

def test_list_all_books(libro_service):
    mock_storage = MagicMock()
    book1 = Book(id=1, title="Book 1", author_id=1, publishing_year=2020, total_pages=300, pages_read=150, genre_id="Fiction", score=4, review="Great book!")
    book2 = Book(id=2, title="Book 2", author_id=1, publishing_year=2021, total_pages=250, pages_read=100, genre_id="Fiction", score=5, review="Excellent!")
    book3 = Book(id=3, title="Book 3", author_id=2, publishing_year=2019, total_pages=200, pages_read=50, genre_id="Non-Fiction", score=3, review="Good read.")
    mock_storage.load_books.return_value = [book1, book2, book3]
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    all_books = service.all_books()
    assert all_books == [book1, book2, book3]

def test_list_authors_books_nonexistent_author(libro_service):
    mock_storage = MagicMock()
    book1 = Book(id=1, title="Book 1", author_id=1, publishing_year=2020, total_pages=300, pages_read=150, genre_id="Fiction", score=4, review="Great book!")
    book2 = Book(id=2, title="Book 2", author_id=1, publishing_year=2021, total_pages=250, pages_read=100, genre_id="Fiction", score=5, review="Excellent!")
    book3 = Book(id=3, title="Book 3", author_id=2, publishing_year=2019, total_pages=200, pages_read=50, genre_id="Non-Fiction", score=3, review="Good read.")
    mock_storage.load_books.return_value = [book1, book2, book3]
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    with pytest.raises(AuthorNotFoundError):
        service.list_authors_books(999)

def test_list_genre_books_nonexistent_genre(libro_service):
    mock_storage = MagicMock()
    book1 = Book(id=1, title="Book 1", author_id=1, publishing_year=2020, total_pages=300, pages_read=150, genre_id="Fiction", score=4, review="Great book!")
    book2 = Book(id=2, title="Book 2", author_id=1, publishing_year=2021, total_pages=250, pages_read=100, genre_id="Fiction", score=5, review="Excellent!")
    book3 = Book(id=3, title="Book 3", author_id=2, publishing_year=2019, total_pages=200, pages_read=50, genre_id="Non-Fiction", score=3, review="Good read.")
    mock_storage.load_books.return_value = [book1, book2, book3]
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    with pytest.raises(GenreNotFoundError):
        service.list_genre_books("Unknown Genre")

def test_list_all_authors(libro_service):
    mock_storage = MagicMock()
    author1 = Author(id=1, name="Author 1")
    author2 = Author(id=2, name="Author 2")
    mock_storage.load_authors.return_value = [author1, author2]
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    all_authors = service.all_authors()
    assert all_authors == [author1, author2]

def test_list_all_genres(libro_service):
    mock_storage = MagicMock()
    genre1 = Genre(id=1, name="Fiction")
    genre2 = Genre(id=2, name="Non-Fiction")
    mock_storage.load_genres.return_value = [genre1, genre2]
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    all_genres = service.all_genres()
    assert all_genres == [genre1, genre2]

def test_list_all_books_empty(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_books.return_value = []
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    all_books = service.all_books()
    assert all_books == []

def test_list_all_authors_empty(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_authors.return_value = []
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    all_authors = service.all_authors()
    assert all_authors == []

def test_list_all_genres_empty(libro_service):
    mock_storage = MagicMock()
    mock_storage.load_genres.return_value = []
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    all_genres = service.all_genres()
    assert all_genres == []

def test_show_book_details(libro_service):
    mock_storage = MagicMock()
    author = Author(id=1, name="Author 1")
    genre = Genre(id=1, name="Fiction")
    book = Book(id=1, title="Test Book", author_id=1, publishing_year=2020, total_pages=300, pages_read=150, genre_id="Fiction", score=4, review="Great book!")
    mock_storage.load_books.return_value = [book]
    mock_storage.load_authors.return_value = [author]
    mock_storage.load_genres.return_value = [genre]
    libro_service.storage = mock_storage
    
    service = LibroService(mock_storage)
    book_details = service.show_book_details(1)
    assert book_details == Book(id=1, title="Test Book", author_id=1, publishing_year=2020, total_pages=300, pages_read=150, genre_id="Fiction", score=4, review="Great book!", author=author, genre=genre)