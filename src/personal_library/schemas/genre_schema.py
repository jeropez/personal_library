from pydantic import BaseModel, Field


class GenreCreate(BaseModel):
    name: str = Field(min_length=1)


class GenreResponse(GenreCreate):
    id: int