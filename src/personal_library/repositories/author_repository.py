from personal_library.supabase_client import supabase


class AuthorRepository:

    @staticmethod
    def get_authors():
        return supabase.table("authors").select("*").execute()

    @staticmethod
    def create_author(data: dict):
        return supabase.table("authors").insert(data).execute()