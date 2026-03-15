# Guía de instalación 

Esta guía explica cómo instalar la aplicación de línea de comandos para gestionar la libreria personal.

## Instalción paso a paso

1️⃣ Clonar el repositorio:

git clone https://github.com/tu-usuario/personal_library.git cd
personal_library

2️⃣ Instalar dependencias con uv:

uv sync –extra dev

3️⃣ Ejecutar la aplicación:

uv run library list-books