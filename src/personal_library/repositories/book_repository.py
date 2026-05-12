from personal_library.supabase_client import supabase


class BookRepository:

    @staticmethod
    def get_books():
        return supabase.table("books").select("*").execute()

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
        return supabase.table("books").insert(data).execute()

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