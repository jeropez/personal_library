# Guía de Usuario

Esta guía explica cómo utilizar la aplicación de línea de comandos para gestionar la libreria personal.

## Ejecutar la aplicación

La aplicación se ejecuta utilizando Python:

```bash
uv run main.py [COMANDO] [INPUTS]
```
## Guia de comandos
📖 Agregar un libro:

uv run library add-book

🔍 Buscar libro por ID:

uv run library find-book 1

📚 Listar libros:

uv run library list-books

❌ Eliminar libro:

uv run library delete-book 1

📈 Actualizar progreso de lectura:

uv run library update-progress 1 150

⭐ Puntuar libro:

uv run library rate-book 1 5

📝 Escribir reseña:

uv run library review-book 1 “Excelente libro”

👤 Gestión de autores:

Agregar autor: uv run library add-author

Listar autores: uv run library list-authors

Libros de un autor: uv run library author-books 1

🏷 Gestión de géneros:

Agregar género: uv run library add-genre

Listar géneros: uv run library list-genres

Libros de un género: uv run library genre-books Fantasy

## Ejemplos de salida 

### 1

**Comando:** uv run main.py list-books

**Salida esperada:**{'title': 'El Principito', 'author': 'Antoine de Saint-Exupéry', 'genre': 'Ficción'}
{'title': '1984', 'author': 'George Orwell', 'genre': 'Distopía'}

### 2

**Comando:** uv run main.py add-book "" "Autor" "Ficción"

**Salida esperada:** Error: Title cannot be empty

### 3

**Comando:** uv run main.py add-book "Dune" "Frank Herbert" "Ciencia ficción"
             uv run main.py list-books

**Salida esperada:** Book added successfully

{'title': 'Dune', 'author': 'Frank Herbert', 'genre': 'Ciencia ficción'}



