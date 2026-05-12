from personal_library.supabase_client import supabase


class GenreRepository:

    @staticmethod
    def get_genres():
        return supabase.table("genres").select("*").execute()

    @staticmethod
    def create_genre(data: dict):
        return supabase.table("genres").insert(data).execute()