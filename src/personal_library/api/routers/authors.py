from fastapi import APIRouter

from personal_library.schemas.author_schema import (
    AuthorCreate,
    AuthorResponse,
)
from personal_library.api.services.author_api_services import AuthorService

router = APIRouter(prefix="/authors", tags=["Authors"])


@router.get("/", response_model=list[AuthorResponse])
def get_authors():
    response = AuthorService.get_authors()
    return response.data


@router.post("/", response_model=AuthorResponse)
def create_author(author: AuthorCreate):
    response = AuthorService.create_author(author.model_dump())
    return response.data[0]