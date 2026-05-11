# API Reference

## Arquitectura de referencia

```mermaid
flowchart LR

Models --> Services
Services --> Storage
Storage --> JSON
```

## Models

### Book

::: personal_library.models.book

### Author

::: personal_library.models.author

### Genre

::: personal_library.models.genre

## Services

### Book Service

::: personal_library.services.book_service

### Author Service

::: personal_library.services.author_service

### Genre Service

::: personal_library.services.genre_service