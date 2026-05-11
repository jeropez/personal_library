# Guía de Usuario

Esta guía explica cómo utilizar la aplicación de línea de comandos para gestionar la libreria personal.

## Ejecutar la aplicación

La aplicación se ejecuta utilizando Python:

```bash
uv run main.py [COMANDO] [INPUTS]
```

!!! tip
    Usa el comando help para visualizar todos los comandos disponibles.

## Guía de comandos

### 📖 Agregar un libro

```bash
uv run library add-book
```

### 🔍 Buscar libro por ID

```bash
uv run library find-book 1
```

### 📚 Listar libros

```bash
uv run library list-books
```

### ❌ Eliminar libro

```bash
uv run library delete-book 1
```

### 📈 Actualizar progreso de lectura

```bash
uv run library update-progress 1 150
```

### ⭐ Puntuar libro

```bash
uv run library rate-book 1 5
```

### 📝 Escribir reseña

```bash
uv run library review-book 1 "Excelente libro"
```

## 👤 Gestión de autores

### Agregar autor

```bash
uv run library add-author
```

### Listar autores

```bash
uv run library list-authors
```

### Libros de un autor

```bash
uv run library author-books 1
```

## 🏷 Gestión de géneros

### Agregar género

```bash
uv run library add-genre
```

### Listar géneros

```bash
uv run library list-genres
```

### Libros de un género

```bash
uv run library genre-books Fantasy
```

## Ejemplos de salida

### 1️⃣ Listar libros

#### Comando

```bash
uv run main.py list-books
```

#### Salida esperada

```text
{'title': 'El Principito', 'author': 'Antoine de Saint-Exupéry', 'genre': 'Ficción'}

{'title': '1984', 'author': 'George Orwell', 'genre': 'Distopía'}
```

---

### 2️⃣ Error de validación

#### Comando

```bash
uv run main.py add-book "" "Autor" "Ficción"
```

#### Salida esperada

```text
Error: Title cannot be empty
```

---

### 3️⃣ Agregar libro

#### Comando

```bash
uv run main.py add-book "Dune" "Frank Herbert" "Ciencia ficción"

uv run main.py list-books
```

#### Salida esperada

```text
Book added successfully

{'title': 'Dune', 'author': 'Frank Herbert', 'genre': 'Ciencia ficción'}
```


