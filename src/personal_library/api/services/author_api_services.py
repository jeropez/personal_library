from personal_library.repositories.author_repository import AuthorRepository


class AuthorService:

    @staticmethod
    def get_authors():
        return AuthorRepository.get_authors()

    @staticmethod
    def create_author(author_data: dict):
        return AuthorRepository.create_author(author_data)