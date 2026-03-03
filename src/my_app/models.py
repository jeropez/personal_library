from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Book:
    """ Represents a book in the reading tracking application.
    """
    id: int
    title: str
    author_id: int
    publishing_year: int
    total_pages: int
    pages_read: int
    genre_id: str
    score: Optional[int]  # 1–5
    review: Optional[str]
    author: Author | None = None
    genre: Genre | None = None

@dataclass
class Author:
    """ Represents an author in the reading tracking application.
    """
    id: int
    name: str
    nationality: Optional[str] = None
    books: List[Book] = None

@dataclass
class Genre:
    """ Represents a genre in the reading tracking application.
    """
    id: int
    name: str
    books: List[Book] = None