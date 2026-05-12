from personal_library.repositories.genre_repository import (
    GenreRepository,
)


class GenreAPIService:

    @staticmethod
    def get_genres():
        return GenreRepository.get_genres()

    @staticmethod
    def create_genre(genre_data: dict):
        return GenreRepository.create_genre(
            genre_data
        )
    