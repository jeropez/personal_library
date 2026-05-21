from personal_library.repositories.book_repository import (
    BookRepository,
)


class BookAPIService:

    @staticmethod
    def get_books():
        return BookRepository.get_books()

    @staticmethod
    def get_book(book_id: int):
        return BookRepository.get_book(book_id)

    @staticmethod
    def create_book(book_data: dict):
        return BookRepository.create_book(book_data)

    @staticmethod
    def update_book(book_id: int, data: dict):
        return BookRepository.update_book(
            book_id,
            data,
        )

    @staticmethod
    def delete_book(book_id: int):
        return BookRepository.delete_book(book_id)

    @staticmethod
    def update_review(book_id: int, review: str):
        return BookRepository.update_review(
            book_id,
            review,
        )

    @staticmethod
    def update_score(book_id: int, score: int):
        return BookRepository.update_score(
            book_id,
            score,
        )

    @staticmethod
    def update_progress(
        book_id: int,
        read_pages: int,
    ):
        return BookRepository.update_progress(
            book_id,
            read_pages,
        )

    @staticmethod
    def get_books_by_author(author_id: int):
        return BookRepository.get_books_by_author(
            author_id,
        )

    @staticmethod
    def get_books_by_genre(genre_id: int):
        return BookRepository.get_books_by_genre(
            genre_id,
        )