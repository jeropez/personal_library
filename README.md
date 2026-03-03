📚 PERSONAL LIBRARY MANAGER

Aplicación de gestión de biblioteca personal desarrollada en Python.
Permite administrar libros, autores y géneros, llevar seguimiento de
lectura, asignar puntuaciones y escribir reseñas desde la terminal.

  --------------------
  🚀 CARACTERÍSTICAS
  --------------------

📖 Gestión de Libros - Agregar libros - Buscar libro por ID - Listar
todos los libros - Eliminar libro por ID - Actualizar progreso de
lectura (páginas leídas) - Asignar puntuación (1–5) - Escribir reseña -
Mostrar todos los detalles de un libro

✍ Gestión de Autores - Agregar autor - Buscar autor por ID - Listar
todos los autores - Listar todos los libros de un autor

🏷 Gestión de Géneros - Crear género - Buscar género por ID o nombre -
Listar todos los géneros - Listar libros de un género

  ----------------
  🏗 ARQUITECTURA
  ----------------

El proyecto sigue principios de Clean Architecture y separación de
responsabilidades.

Estructura:

src/my_app/ - models.py -> Entidades (Book, Author, Genre) - services.py
-> Lógica de negocio - storage.py -> Persistencia en JSON - cli.py ->
Interfaz de línea de comandos - exceptions.py -> Excepciones
personalizadas

Separación clara entre: - Dominio - Persistencia - Interfaz - Manejo de
errores

  ---------------
  ⚙ INSTALACIÓN
  ---------------

1️⃣ Clonar el repositorio:

git clone https://github.com/tu-usuario/personal_library.git cd
personal_library

2️⃣ Instalar dependencias con uv:

uv sync –extra dev

3️⃣ Ejecutar la aplicación:

uv run library list-books

  ------------------------
  🖥 USO DE LA APLICACIÓN
  ------------------------

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

  ------------
  🧪 TESTING
  ------------

El proyecto incluye más de 10 pruebas unitarias usando pytest.

Ejecutar pruebas:

uv run pytest

Todas las pruebas deben pasar correctamente.

  -----------
  🔎 LINTER
  -----------

Se utiliza ruff para análisis estático de código.

uv run ruff check .

  -----------------
  💾 PERSISTENCIA
  -----------------

Los datos se almacenan en archivos JSON dentro de la carpeta:

data/

Archivos utilizados: - libros.json - authors.json - genres.json

  -------------------------------
  🧠 VALIDACIONES IMPLEMENTADAS
  -------------------------------

-   No se permite agregar libros con autor inexistente
-   No se permite agregar libros con género inexistente
-   Las páginas leídas no pueden superar el total
-   El puntaje debe estar entre 1 y 5
-   No se permiten IDs duplicados
-   Manejo de errores mediante excepciones personalizadas

  ---------------
  📦 REQUISITOS
  ---------------

-   Python >= 3.11
-   uv
-   pytest
-   typer
-   rich
-   ruff

  ----------------------
  👨‍💻 DESCRIPCIÓN FINAL
  ----------------------

Proyecto desarrollado aplicando principios de:

-   Clean Code
-   Arquitectura en capas
-   Testing automatizado
-   Manejo explícito de errores
-   CLI profesional con Rich y Typer

Estado del proyecto: ✔ Tests automatizados ✔ Validaciones completas ✔
CLI interactiva ✔ Persistencia en JSON ✔ Linter configurado
