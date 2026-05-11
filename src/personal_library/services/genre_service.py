from personal_library.models import Genre


class GenreService:
    def __init__(self, storage):
        self.storage = storage

    def add_genre(self, genre: Genre) -> None:
        self.storage.add_genre(genre)

    def list_genres(self) -> list[Genre]:
        return self.storage.list_genres()