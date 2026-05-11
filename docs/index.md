# Personal Library Managment CLI

Bienvenido a la documentación oficial de **Personal Library Managment**, una aplicación
de línea de comandos desarrollada en Python para gestionar una libreria personal utilizando
principios de **Clean Code**, **Testing** y **Arquitectura modular**.

## Características

- CLI moderna basada en **Typer**
- Persistencia de datos en archivo JSON
- Arquitectura modular (`src layout`)
- Pruebas unitarias con `pytest`
- Uso de **mocks** para aislar dependencias
- Excepciones personalizadas
- Principios de diseño **SOLID**
- Documentación generada automáticamente
- Análisis de complejidad ciclomática con **Radon**
- Integración continua con GitHub Actions

## Estructura del sistema

```bash
personal_library/
├── README.md
├── pyproject.toml
├── uv.lock
├── main.py
├── mkdocs.yml
├── data
│   ├── libros.json
│   ├── autores.json
│   └── generos.json
├── docs
│   ├── index.md
│   ├── guia-instalacion.md
│   ├── guia-desarrollo.md
│   ├── architecture.md
│   ├── reference.md
│   └── user_guide
│       ├── guia_usuario.md
│       └── persistance.md
├── src
│   └── personal_library
│       ├── __init__.py
│       ├── cli.py
│       ├── exceptions.py
│       ├── models
│       │   ├── __init__.py
│       │   ├── author.py
│       │   ├── book.py
│       │   └── genre.py
│       ├── services
│       │   ├── __init__.py
│       │   ├── author_service.py
│       │   ├── book_service.py
│       │   └── genre_service.py
│       └── storage.py
└── tests
    ├── __init__.py
    ├── conftest.py
    └── test_services.py
```

## Flujo general del sistema

```mermaid
flowchart TD

User --> CLI
CLI --> Services
Services --> Models
Services --> Storage
Storage --> JSON
```

## Documentación

Esta documentación está dividida en tres secciones principales:

| Sección         | Descripción               |
| --------------- | ------------------------- |
| Guía de Usuario | Cómo usar la aplicación   |
| Instalación     | Cómo instalar el proyecto |
| API             | Documentación del código  |

!!! tip "Recomendación"
    Si es tu primera vez usando el proyecto, comienza por la sección **Guía de Usuario**.