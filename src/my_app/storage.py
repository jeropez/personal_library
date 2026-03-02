import json
from pathlib import Path
from typing import List
from .models import Libro, Autor, Genero
from typing import Protocol

class Storage(Protocol):
    """ Defines the interface for data storage operations in the application.
    """
    def load_books(self) -> List[Libro]: ...
    def save_books(self, libros: List[Libro]) -> None: ...
    def load_authors(self) -> List[Autor]: ...
    def save_authors(self, autores: List[Autor]) -> None: ...
    def load_genres(self) -> List[Genero]: ...
    def save_genres(self, generos: List[Genero]) -> None: ...

class JsonStorage:
    """ Implementación de Storage que utiliza archivos JSON para persistencia.
    """
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.libros_file = base_path / "libros.json"
        self.autores_file = base_path / "autores.json"
        self.generos_file = base_path / "generos.json"

    def load_books(self) -> List[Libro]:
        if not self.libros_file.exists():
            return []
        with open(self.libros_file, "r", encoding="utf-8") as f:
            libros_data = json.load(f)
            return [Libro(**libro) for libro in libros_data]

    def save_books(self, libros: List[Libro]) -> None:
        with open(self.libros_file, "w", encoding="utf-8") as f:
            json.dump([libro.__dict__ for libro in libros], f, ensure_ascii=False, indent=4)

    def load_authors(self) -> List[Autor]:
        if not self.autores_file.exists():
            return []
        with open(self.autores_file, "r", encoding="utf-8") as f:
            autores_data = json.load(f)
            return [Autor(**autor) for autor in autores_data]

    def save_authors(self, autores: List[Autor]) -> None:
        with open(self.autores_file, "w", encoding="utf-8") as f:
            json.dump([autor.__dict__ for autor in autores], f, ensure_ascii=False, indent=4)

    def load_genres(self) -> List[Genero]:
        if not self.generos_file.exists():
            return []
        with open(self.generos_file, "r", encoding="utf-8") as f:
            generos_data = json.load(f)
            return [Genero(**genero) for genero in generos_data]

    def save_genres(self, generos: List[Genero]) -> None:
        with open(self.generos_file, "w", encoding="utf-8") as f:
            json.dump([genero.__dict__ for genero in generos], f, ensure_ascii=False, indent=4)
    