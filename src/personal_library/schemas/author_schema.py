from pydantic import BaseModel, Field


class AuthorCreate(BaseModel):
    name: str = Field(min_length=1)
    nationality: str = Field(min_length=1)


class AuthorResponse(AuthorCreate):
    id: int