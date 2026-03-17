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

## Arquitectura del sistema

```mermaid
flowchart LR

    CLI["CLI (cli.py)<br/>Typer + Rich<br/>Interfaz de usuario"]

    SERVICES["Services (services.py)<br/>Lógica de negocio<br/>Validaciones<br/>Reglas del dominio"]

    MODELS["Models (models.py)<br/>Book<br/>Author<br/>Genre<br/>Dataclasses"]

    STORAGE["Storage (storage.py)<br/>Persistencia<br/>Lectura / Escritura"]

    DATA["JSON Files (data/)<br/>libros.json<br/>autores.json<br/>generos.json"]

    EXCEPTIONS["Exceptions (exceptions.py)<br/>BookNotFoundError<br/>AuthorNotFoundError<br/>GenreNotFoundError<br/>InvalidScoreError<br/>etc."]

    CLI --> SERVICES
    SERVICES --> STORAGE
    STORAGE --> DATA
    SERVICES --> MODELS
    SERVICES --> EXCEPTIONS
    CLI --> EXCEPTIONS
```

## Estructura del sistema
```bash
personal_library/
├── README.md
├── pyproject.toml
├── uv.lock
├── main.py
├── data
│   ├── libros.json
│   ├── autores.json
│   └── generos.json
├── src
│   └── my_app
│       ├── __init__.py
│       ├── cli.py
│       ├── models.py
│       ├── services.py
│       ├── storage.py
│       └── exceptions.py
└── tests
    ├── __init__.py
    ├── conftest.py
    └── test_services.py
```

## Flujo general de ejecución
```mermaid
sequenceDiagram
    actor User
    participant CLI as "CLI (cli.py)"
    participant Service as "LibroService (services.py)"
    participant Storage as "Storage (storage.py)"
    participant Data as "JSON Files (data/)"

    User->>CLI: "Ejecuta comando (ej. add-book)"
    CLI->>Service: "Llama método del servicio"
    Service->>Storage: "Solicita datos (load_books / load_authors / load_genres)"
    Storage->>Data: "Lee archivos JSON"
    Data-->>Storage: "Devuelve datos"
    Storage-->>Service: "Retorna objetos cargados"

    Service->>Service: "Aplica validaciones y lógica de negocio"

    Service->>Storage: "Guarda cambios (save_books / save_authors / save_genres)"
    Storage->>Data: "Escribe en archivos JSON"
    Data-->>Storage: "Confirmación"

    Storage-->>Service: "Operación completada"
    Service-->>CLI: "Resultado de la operación"
    CLI-->>User: "Muestra resultado con Rich"
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

