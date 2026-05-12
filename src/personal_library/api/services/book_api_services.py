from personal_library.repositories.book_repository import BookRepository


class BookService:

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
    def update_book(book_id: int, book_data: dict):
        return BookRepository.update_book(book_id, book_data)

    @staticmethod
    def delete_book(book_id: int):
        return BookRepository.delete_book(book_id)