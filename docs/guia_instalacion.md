# Guía de instalación

Esta guía explica cómo instalar la aplicación de línea de comandos para gestionar la libreria personal.

## Instalación paso a paso

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/jeropez/personal_library.git
cd personal_library
```

### 2️⃣ Instalar dependencias con uv

=== "Linux / Mac"

    ```bash
    uv sync
    ```

=== "Windows"

    ```powershell
    uv sync
    ```

### 3️⃣ Ejecutar la aplicación

```bash
uv run main.py --help
```

### 4️⃣ Ejecutar pruebas

```bash
uv run pytest
```

### 5️⃣ Ejecutar análisis de complejidad

```bash
uv run radon cc src -a
```

!!! tip
    Asegúrate de tener Python 3.11 o superior instalado.