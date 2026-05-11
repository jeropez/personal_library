class AppError(Exception):
    """ Base class for all application-specific errors.
    """
    pass

class BookError(AppError):
    """ Errors related to book operations.
    """
    pass

class AuthorError(AppError):
    """ Errors related to author operations.
    """
    pass

class GenreError(AppError):
    """ Errors related to genre operations.
    """
    pass

class StorageError(AppError):
    """ Errors related to data storage operations.
    """
    pass

class ValidationError(AppError):
    """ Errors related to data validation.
    """

    pass    

class NotFoundError(AppError):
    """ Errors related to resources not being found.
    """
    pass    

class DuplicateError(AppError):
    """ Errors related to duplicate entries.
    """
    pass

class BookNotFoundError(NotFoundError):
    """ Error to indicate that a book was not found.
    """
    def __init__(self, book_id: int):
        super().__init__(f"Book with ID {book_id} not found.")

class AuthorNotFoundError(NotFoundError):
    """ Error to indicate that an author was not found.
    """
    def __init__(self, author_id: int):
        super().__init__(f"Author with ID {author_id} not found.")

class GenreNotFoundError(NotFoundError):
    """ Error to indicate that a genre was not found.
    """
    def __init__(self, genre_id: int):
        super().__init__(f"Genre with ID {genre_id} not found.")

class BookAlreadyExistsError(DuplicateError):
    """ Error to indicate that a book with the same ID already exists.
    """
    def __init__(self, book_id: int):
        super().__init__(f"Book with ID {book_id} already exists.")

class AuthorAlreadyExistsError(DuplicateError):
    """ Error to indicate that an author with the same ID already exists.
    """
    def __init__(self, author_id: int):
        super().__init__(f"Author with ID {author_id} already exists.")

class GenreAlreadyExistsError(DuplicateError):
    """ Error to indicate that a genre with the same ID already exists.
    """
    def __init__(self, genre_id: int):
        super().__init__(f"Genre with ID {genre_id} already exists.")

class PagesReadExceedsTotalError(ValidationError):
    """ Error to indicate that the number of pages read exceeds the total pages of a book.
    """
    def __init__(self, pages_read: int, total_pages: int):
        super().__init__(f"Pages read ({pages_read}) cannot exceed total pages ({total_pages}).")

class InvalidScoreError(ValidationError):
    """ Error to indicate that a provided score is invalid (not in the range 1–5).
    """
    def __init__(self, score: int):
        super().__init__(f"Score {score} is invalid. Score must be between 1 and 5.")

class InvalidInputError(ValidationError):
    """ Error to indicate that the provided input data is invalid.
    """
    def __init__(self, message: str):
        super().__init__(message)