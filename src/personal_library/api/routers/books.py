from fastapi import APIRouter, HTTPException

from personal_library.schemas.book_schema import (
    BookCreate,
    BookUpdate,
    BookResponse,
    BookReviewUpdate,
    BookScoreUpdate,
    BookProgressUpdate,
)

from src.personal_library.api.services.book_api_services import (
    BookAPIService,
)

router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


@router.get("/", response_model=list[BookResponse])
def get_books():
    response = BookAPIService.get_books()

    return response.data


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    response = BookAPIService.get_book(book_id)

    if not response.data:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )

    return response.data[0]


@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate):
    response = BookAPIService.create_book(
        book.model_dump()
    )

    return response.data[0]


@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book: BookUpdate,
):
    response = BookAPIService.update_book(
        book_id,
        book.model_dump(exclude_unset=True),
    )

    return response.data[0]


@router.delete("/{book_id}")
def delete_book(book_id: int):
    BookAPIService.delete_book(book_id)

    return {
        "message": "Book deleted successfully"
    }


@router.patch("/{book_id}/review")
def update_review(
    book_id: int,
    data: BookReviewUpdate,
):
    response = BookAPIService.update_review(
        book_id,
        data.review,
    )

    return response.data[0]


@router.patch("/{book_id}/score")
def update_score(
    book_id: int,
    data: BookScoreUpdate,
):
    response = BookAPIService.update_score(
        book_id,
        data.score,
    )

    return response.data[0]


@router.patch("/{book_id}/progress")
def update_progress(
    book_id: int,
    data: BookProgressUpdate,
):
    response = BookAPIService.update_progress(
        book_id,
        data.read_pages,
    )

    return response.data[0]


@router.get("/author/{author_id}")
def get_books_by_author(author_id: int):
    response = BookAPIService.get_books_by_author(
        author_id
    )

    return response.data


@router.get("/genre/{genre_id}")
def get_books_by_genre(genre_id: int):
    response = BookAPIService.get_books_by_genre(
        genre_id
    )

    return response.data