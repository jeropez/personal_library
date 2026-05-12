from fastapi import APIRouter

from personal_library.schemas.genre_schema import (
    GenreCreate,
    GenreResponse,
)
from personal_library.api.services.genre_api_services import (
    GenreAPIService,
)

router = APIRouter(
    prefix="/genres",
    tags=["Genres"],
)


@router.get("/", response_model=list[GenreResponse])
def get_genres():
    response = GenreAPIService.get_genres()

    return response.data


@router.post("/", response_model=GenreResponse)
def create_genre(genre: GenreCreate):
    response = GenreAPIService.create_genre(
        genre.model_dump()
    )

    return response.data[0]