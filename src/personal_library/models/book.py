from dataclasses import dataclass


@dataclass
class Book:
    """Represents a book in the personal library."""
    id: int
    title: str
    author_id: int
    genre_id: int
    published_year: int
    total_pages: int
    read_pages: int
    score: int | None = None
    review: str | None = None

    def __post_init__(self):
        self._validate_title()
        self._validate_pages()
        self._validate_score()

    def _validate_title(self):
        if not self.title.strip():
            raise ValueError("Title cannot be empty")

    def _validate_pages(self):
        if self.total_pages <= 0:
            raise ValueError("Total pages must be greater than 0")

        if self.read_pages < 0:
            raise ValueError("Read pages cannot be negative")

        if self.read_pages > self.total_pages:
            raise ValueError("Read pages cannot exceed total pages")

    def _validate_score(self):
        if self.score is not None and not 1 <= self.score <= 5:
            raise ValueError("Score must be between 1 and 5")