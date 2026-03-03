import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

from my_app.services import LibroService
from my_app.storage import JsonStorage

app = typer.Typer()
console = Console()

storage = JsonStorage("data")
service = LibroService(storage)

@app.command()
def add_book():
    console.print(Panel("Agregar nuevo libro", style="bold green"))

    title = typer.prompt("Título")
    author_id = typer.prompt("ID del autor", type=int)
    year = typer.prompt("Año de publicación", type=int)
    total_pages = typer.prompt("Total de páginas", type=int)
    genre = typer.prompt("Género")

    service.add_book_manual(
        title=title,
        author_id=author_id,
        publishing_year=year,
        total_pages=total_pages,
        genre_id=genre,
    )

    console.print("✅ Libro agregado correctamente", style="bold green")

@app.command()
def list_books():
    books = service.all_books()

    table = Table(title="Lista de Libros", box=box.ROUNDED)
    table.add_column("ID", justify="center")
    table.add_column("Título")
    table.add_column("Autor")
    table.add_column("Progreso")

    for book in books:
        progress = f"{book.pages_read}/{book.total_pages}"
        table.add_row(str(book.id), book.title, str(book.author_id), progress)

    console.print(table)

@app.command()
def find_book(book_id: int):
    book = service.get_book(book_id)

    panel = Panel.fit(
        f"[bold]{book.title}[/bold]\n\n"
        f"Autor ID: {book.author_id}\n"
        f"Año: {book.publishing_year}\n"
        f"Páginas: {book.pages_read}/{book.total_pages}\n"
        f"Puntaje: {book.score}\n"
        f"Reseña: {book.review}",
        title="Detalles del Libro",
        border_style="cyan",
    )

    console.print(panel)

@app.command()
def delete_book(book_id: int):
    service.delete_book(book_id)
    console.print("🗑 Libro eliminado correctamente", style="bold red")

@app.command()
def add_author():
    name = typer.prompt("Nombre del autor")
    service.add_author_manual(name)
    console.print("✅ Autor agregado", style="green")

@app.command()
def list_authors():
    authors = service.all_authors()

    table = Table(title="Autores", box=box.ROUNDED)
    table.add_column("ID")
    table.add_column("Nombre")

    for author in authors:
        table.add_row(str(author.id), author.name)

    console.print(table)

@app.command()
def author_books(author_id: int):
    books = service.list_authors_books(author_id)

    table = Table(title="Libros del Autor", box=box.ROUNDED)
    table.add_column("ID")
    table.add_column("Título")

    for book in books:
        table.add_row(str(book.id), book.title)

    console.print(table)

@app.command()
def add_genre():
    name = typer.prompt("Nombre del género")
    service.add_genre_manual(name)
    console.print("✅ Género creado", style="green")

@app.command()
def list_genres():
    genres = service.all_genres()

    table = Table(title="Géneros", box=box.ROUNDED)
    table.add_column("ID")
    table.add_column("Nombre")

    for genre in genres:
        table.add_row(str(genre.id), genre.name)

    console.print(table)

@app.command()
def genre_books(genre: str):
    books = service.list_genre_books(genre)

    table = Table(title="Libros del Género", box=box.ROUNDED)
    table.add_column("ID")
    table.add_column("Título")

    for book in books:
        table.add_row(str(book.id), book.title)

    console.print(table)

@app.command()
def rate_book(book_id: int, score: int):
    service.rate_book(book_id, score)
    console.print("⭐ Puntaje actualizado", style="yellow")

@app.command()
def update_progress(book_id: int, pages: int):
    service.update_pages_read(book_id, pages)
    console.print("📖 Progreso actualizado", style="blue")

@app.command()
def review_book(book_id: int):
    review = typer.prompt("Escribe tu reseña")
    service.review_book(book_id, review)
    console.print("📝 Reseña guardada", style="magenta")

