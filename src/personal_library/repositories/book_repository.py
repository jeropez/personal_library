from personal_library.supabase_client import supabase


class BookRepository:

    @staticmethod
    def get_books():
        return (
            supabase
            .table("books")
            .select("*")
            .execute()
        )

    @staticmethod
    def get_book(book_id: int):
        return (
            supabase
            .table("books")
            .select("*")
            .eq("id", book_id)
            .execute()
        )

    @staticmethod
    def create_book(data: dict):
        return (
            supabase
            .table("books")
            .insert(data)
            .execute()
        )

    @staticmethod
    def update_book(book_id: int, data: dict):
        return (
            supabase
            .table("books")
            .update(data)
            .eq("id", book_id)
            .execute()
        )

    @staticmethod
    def delete_book(book_id: int):
        return (
            supabase
            .table("books")
            .delete()
            .eq("id", book_id)
            .execute()
        )

    @staticmethod
    def update_review(book_id: int, review: str):
        return (
            supabase
            .table("books")
            .update({"review": review})
            .eq("id", book_id)
            .execute()
        )

    @staticmethod
    def update_score(book_id: int, score: int):
        return (
            supabase
            .table("books")
            .update({"score": score})
            .eq("id", book_id)
            .execute()
        )

    @staticmethod
    def update_progress(book_id: int, read_pages: int):
        return (
            supabase
            .table("books")
            .update({"read_pages": read_pages})
            .eq("id", book_id)
            .execute()
        )

    @staticmethod
    def get_books_by_author(author_id: int):
        return (
            supabase
            .table("books")
            .select("*")
            .eq("author_id", author_id)
            .execute()
        )

    @staticmethod
    def get_books_by_genre(genre_id: int):
        return (
            supabase
            .table("books")
            .select("*")
            .eq("genre_id", genre_id)
            .execute()
        )