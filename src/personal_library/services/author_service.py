from personal_library.models import Author


class AuthorService:
    def __init__(self, storage):
        self.storage = storage

    def add_author(self, author: Author) -> None:
        self.storage.add_author(author)

    def list_authors(self) -> list[Author]:
        return self.storage.list_authors()