from fastapi import FastAPI

from personal_library.api.routers.books import router as books_router
from personal_library.api.routers.authors import router as authors_router
from personal_library.api.routers.genres import router as genres_router

app = FastAPI(
    title="Personal Library API",
    version="1.0.0",
)

app.include_router(books_router)
app.include_router(authors_router)
app.include_router(genres_router)


@app.get("/")
def root():
    return {
        "message": "Personal Library API running"
    }