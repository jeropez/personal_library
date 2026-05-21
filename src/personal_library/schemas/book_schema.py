from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author_id: int
    genre_id: int
    published_year: int
    total_pages: int
    read_pages: int = 0
    score: int | None = None
    review: str | None = None


class BookUpdate(BaseModel):
    title: str | None = None
    author_id: int | None = None
    genre_id: int | None = None
    published_year: int | None = None
    total_pages: int | None = None
    read_pages: int | None = None
    score: int | None = None
    review: str | None = None


class BookReviewUpdate(BaseModel):
    review: str


class BookScoreUpdate(BaseModel):
    score: int = Field(ge=1, le=5)


class BookProgressUpdate(BaseModel):
    read_pages: int = Field(ge=0)


class BookResponse(BookCreate):
    id: int