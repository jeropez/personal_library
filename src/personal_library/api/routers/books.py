from fastapi import APIRouter, HTTPException

from personal_library.schemas.book_schema import (
    BookCreate,
    BookUpdate,
    BookResponse,
)
from personal_library.api.services.book_api_services import BookService

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookResponse])
def get_books():
    response = BookService.get_books()
    return response.data


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    response = BookService.get_book(book_id)

    if not response.data:
        raise HTTPException(status_code=404, detail="Book not found")

    return response.data[0]


@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate):
    response = BookService.create_book(book.model_dump())
    return response.data[0]


@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate):
    response = BookService.update_book(
        book_id,
        book.model_dump(exclude_unset=True)
    )

    return response.data[0]


@router.delete("/{book_id}")
def delete_book(book_id: int):
    BookService.delete_book(book_id)

    return {
        "message": "Book deleted successfully"
    }