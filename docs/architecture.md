# Arquitectura del sistema

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


Este proyecto sigue una arquitectura por capas (layered architecture) que separa responsabilidades para mejorar la mantenibilidad, escalabilidad y claridad del código.

---

## Vista general

```mermaid
flowchart LR

    subgraph Interface
        CLI[CLI]
    end

    subgraph Business
        Service[LibroService]
    end

    subgraph Persistence
        Storage[Storage]
    end

    subgraph Data
        Books[(books.json)]
        Authors[(authors.json)]
        Genres[(genres.json)]
    end

    CLI --> Service
    Service --> Storage

    Storage --> Books
    Storage --> Authors
    Storage --> Genres
```

## Descripción de las capas

### CLI (Interfaz)


Se encarga de:

- Recibir comandos del usuario

- Validar parámetros de entrada básicos

- Invocar los métodos del servicio

**Ejemplo:** add_book(title, author, genre)

### Service (Lógica de negocio)

Contiene la lógica principal de la aplicación:

- Creación de entidades

- Validaciones de negocio

- Orquestación de operaciones

**Ejemplo:** LibroService.add_book()

### Storage (Persistencia)

Encapsula el acceso a datos:

- Lectura de archivos JSON

- Escritura de archivos JSON

- Manejo de múltiples recursos

### Data (Almacenamiento)

El sistema utiliza archivos JSON separados por entidad:

- books.json

- authors.json

- genres.json

Esto permite:

- Separación de datos

- Mejor organización

- Escalabilidad

## Flujo de ejecucion
```mermaid
sequenceDiagram
    actor User
    participant CLI
    participant Service
    participant Storage
    participant JSON

    User->>CLI: Ejecuta comando
    CLI->>Service: Llama método
    Service->>Storage: Solicita datos
    Storage->>JSON: Lee archivo
    JSON-->>Storage: Retorna datos
    Storage-->>Service: Datos
    Service->>Storage: Guarda cambios
    Storage->>JSON: Escribe archivo
```

## Desiciones de diseño

### Uso de src layout
El proyecto utiliza la estructura src/ para:

- Evitar problemas de importación

- Separar código fuente de configuración

### Separación por capas

Cada módulo tiene una responsabilidad única:

- CLI -> interfaz

- Service -> lógica

- Storage -> persistencia

Esto sigue el principio de **Single Responsibility**.

### Modelos con dataclasses

Los modelos se implementan como dataclasses para:

- Reducir código boilerplate

- Facilitar serialización

- Mejorar legibilidad

### Validaciones en modelos

Se utilizan métodos ___post_init___() para validar:

- Datos obligatorios

- Consistencia de objetos