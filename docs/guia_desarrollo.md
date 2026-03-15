# Guía de desarrollo

Esta guía explica el funcionamiento interno de la aplicación de línea de comandos para gestionar la libreria personal.

## Testeo

El proyecto incluye más de 10 pruebas unitarias usando pytest.

Ejecutar pruebas:

uv run pytest

Todas las pruebas deben pasar correctamente.

Se utiliza ruff para análisis estático de código.

uv run ruff check .

## Persistencia

Los datos se almacenan en archivos JSON dentro de la carpeta:

data/

Archivos utilizados: - libros.json - authors.json - genres.json

## Validaciones implementadas

-   No se permite agregar libros con autor inexistente
-   No se permite agregar libros con género inexistente
-   Las páginas leídas no pueden superar el total
-   El puntaje debe estar entre 1 y 5
-   No se permiten IDs duplicados
-   Manejo de errores mediante excepciones personalizadas

## Requisitos

-   Python >= 3.11
-   uv
-   pytest
-   typer
-   rich
-   ruff

