import pytest
from unittest.mock import MagicMock

from personal_library.models.author import Author
from personal_library.models.book import Book
from personal_library.models.genre import Genre
from personal_library.services.book_service import BookService

from personal_library.exceptions import (
    AuthorAlreadyExistsError,
    AuthorNotFoundError,
    BookAlreadyExistsError,
    BookNotFoundError,
    GenreAlreadyExistsError,
    GenreNotFoundError,
    InvalidScoreError,
    PagesReadExceedsTotalError,
)


def create_book(
    book_id=1,
    title="Test Book",
    author_id=1,
    genre_id=1,
    published_year=2020,
    total_pages=300,
    read_pages=150,
    score=4,
    review="Great book!",
):
    return Book(
        id=book_id,
        title=title,
        author_id=author_id,
        genre_id=genre_id,
        published_year=published_year,
        total_pages=total_pages,
        read_pages=read_pages,
        score=score,
        review=review,
    )


def test_add_and_get_book():
    mock_storage = MagicMock()
    mock_storage.load_books.return_value = []

    service = BookService(mock_storage)

    book = create_book()

    service.add_book(book)

    mock_storage.save_books.assert_called_once_with([book])

    mock_storage.load_books.return_value = [book]

    retrieved_book = service.get_book(1)

    assert retrieved_book == book


def test_add_duplicate_book():
    mock_storage = MagicMock()

    book = create_book()

    mock_storage.load_books.return_value = [book]

    service = BookService(mock_storage)

    with pytest.raises(BookAlreadyExistsError):
        service.add_book(book)


def test_get_nonexistent_book():
    mock_storage = MagicMock()
    mock_storage.load_books.return_value = []

    service = BookService(mock_storage)

    with pytest.raises(BookNotFoundError):
        service.get_book(999)


def test_delete_book():
    mock_storage = MagicMock()

    book = create_book()

    mock_storage.load_books.return_value = [book]

    service = BookService(mock_storage)

    service.delete_book(1)

    mock_storage.save_books.assert_called_once_with([])


def test_delete_nonexistent_book():
    mock_storage = MagicMock()
    mock_storage.load_books.return_value = []

    service = BookService(mock_storage)

    with pytest.raises(BookNotFoundError):
        service.delete_book(999)


def test_add_and_get_author():
    mock_storage = MagicMock()
    mock_storage.load_authors.return_value = []

    service = BookService(mock_storage)

    author = Author(id=1, name="Test Author")

    service.add_author(author)

    mock_storage.save_authors.assert_called_once_with([author])

    mock_storage.load_authors.return_value = [author]

    retrieved_author = service.get_author(1)

    assert retrieved_author == author


def test_add_duplicate_author():
    mock_storage = MagicMock()

    author = Author(id=1, name="Test Author")

    mock_storage.load_authors.return_value = [author]

    service = BookService(mock_storage)

    with pytest.raises(AuthorAlreadyExistsError):
        service.add_author(author)


def test_get_nonexistent_author():
    mock_storage = MagicMock()
    mock_storage.load_authors.return_value = []

    service = BookService(mock_storage)

    with pytest.raises(AuthorNotFoundError):
        service.get_author(999)


def test_add_and_get_genre():
    mock_storage = MagicMock()
    mock_storage.load_genres.return_value = []

    service = BookService(mock_storage)

    genre = Genre(id=1, name="Fiction")

    service.add_genre(genre)

    mock_storage.save_genres.assert_called_once_with([genre])

    mock_storage.load_genres.return_value = [genre]

    retrieved_genre = service.get_genre(1)

    assert retrieved_genre == genre


def test_add_duplicate_genre():
    mock_storage = MagicMock()

    genre = Genre(id=1, name="Fiction")

    mock_storage.load_genres.return_value = [genre]

    service = BookService(mock_storage)

    with pytest.raises(GenreAlreadyExistsError):
        service.add_genre(genre)


def test_get_nonexistent_genre():
    mock_storage = MagicMock()
    mock_storage.load_genres.return_value = []

    service = BookService(mock_storage)

    with pytest.raises(GenreNotFoundError):
        service.get_genre(999)


def test_update_pages_read_exceeds_total():
    mock_storage = MagicMock()

    book = create_book()

    mock_storage.load_books.return_value = [book]

    service = BookService(mock_storage)

    with pytest.raises(PagesReadExceedsTotalError):
        service.update_pages_read(1, 350)


def test_rate_book_invalid_score():
    mock_storage = MagicMock()

    book = create_book()

    mock_storage.load_books.return_value = [book]

    service = BookService(mock_storage)

    with pytest.raises(InvalidScoreError):
        service.rate_book(1, 6)


def test_rate_book_nonexistent():
    mock_storage = MagicMock()
    mock_storage.load_books.return_value = []

    service = BookService(mock_storage)

    with pytest.raises(BookNotFoundError):
        service.rate_book(999, 4)


def test_update_pages_read_nonexistent_book():
    mock_storage = MagicMock()
    mock_storage.load_books.return_value = []

    service = BookService(mock_storage)

    with pytest.raises(BookNotFoundError):
        service.update_pages_read(999, 100)


def test_review_book_nonexistent():
    mock_storage = MagicMock()
    mock_storage.load_books.return_value = []

    service = BookService(mock_storage)

    with pytest.raises(BookNotFoundError):
        service.review_book(999, "This is a review.")


def test_list_authors_books():
    mock_storage = MagicMock()

    book1 = create_book(book_id=1, author_id=1)
    book2 = create_book(book_id=2, author_id=1)
    book3 = create_book(book_id=3, author_id=2)

    mock_storage.load_books.return_value = [book1, book2, book3]

    service = BookService(mock_storage)

    authors_books = service.list_authors_books(1)

    assert authors_books == [book1, book2]


def test_list_authors_books_nonexistent_author():
    mock_storage = MagicMock()

    mock_storage.load_books.return_value = []

    service = BookService(mock_storage)

    with pytest.raises(AuthorNotFoundError):
        service.list_authors_books(999)


def test_list_genre_books():
    mock_storage = MagicMock()

    book1 = create_book(book_id=1, genre_id=1)
    book2 = create_book(book_id=2, genre_id=1)
    book3 = create_book(book_id=3, genre_id=2)

    mock_storage.load_books.return_value = [book1, book2, book3]

    service = BookService(mock_storage)

    genre_books = service.list_genre_books(1)

    assert genre_books == [book1, book2]


def test_list_genre_books_nonexistent_genre():
    mock_storage = MagicMock()

    mock_storage.load_books.return_value = []

    service = BookService(mock_storage)

    with pytest.raises(GenreNotFoundError):
        service.list_genre_books(999)


def test_list_all_books():
    mock_storage = MagicMock()

    book1 = create_book(book_id=1)
    book2 = create_book(book_id=2)
    book3 = create_book(book_id=3)

    mock_storage.load_books.return_value = [book1, book2, book3]

    service = BookService(mock_storage)

    all_books = service.all_books()

    assert all_books == [book1, book2, book3]


def test_list_all_books_empty():
    mock_storage = MagicMock()

    mock_storage.load_books.return_value = []

    service = BookService(mock_storage)

    all_books = service.all_books()

    assert all_books == []


def test_list_all_authors():
    mock_storage = MagicMock()

    author1 = Author(id=1, name="Author 1")
    author2 = Author(id=2, name="Author 2")

    mock_storage.load_authors.return_value = [author1, author2]

    service = BookService(mock_storage)

    all_authors = service.all_authors()

    assert all_authors == [author1, author2]


def test_list_all_authors_empty():
    mock_storage = MagicMock()

    mock_storage.load_authors.return_value = []

    service = BookService(mock_storage)

    all_authors = service.all_authors()

    assert all_authors == []


def test_list_all_genres():
    mock_storage = MagicMock()

    genre1 = Genre(id=1, name="Fiction")
    genre2 = Genre(id=2, name="Non-Fiction")

    mock_storage.load_genres.return_value = [genre1, genre2]

    service = BookService(mock_storage)

    all_genres = service.all_genres()

    assert all_genres == [genre1, genre2]


def test_list_all_genres_empty():
    mock_storage = MagicMock()

    mock_storage.load_genres.return_value = []

    service = BookService(mock_storage)

    all_genres = service.all_genres()

    assert all_genres == []


def test_show_book_details():
    mock_storage = MagicMock()

    author = Author(id=1, name="Author 1")
    genre = Genre(id=1, name="Fiction")

    book = create_book()

    mock_storage.load_books.return_value = [book]
    mock_storage.load_authors.return_value = [author]
    mock_storage.load_genres.return_value = [genre]

    service = BookService(mock_storage)

    book_details = service.show_book_details(1)

    assert book_details.title == "Test Book"
    assert book_details.author_id == 1
    assert book_details.genre_id == 1