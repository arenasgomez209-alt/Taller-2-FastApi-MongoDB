# Cambios Realizados

De acuerdo a lo solicitado y las actividades propuestas en la imagen, se han realizado los siguientes cambios sin modificar los archivos de código preexistentes (`database.py` y demás):

## Clase 1: Entorno y Arquitectura
- **Creación de `requirements.txt`**: Se agregó el archivo con las dependencias necesarias para el proyecto (FastAPI, Uvicorn, Motor, Pydantic, python-dotenv).
- **Creación de `models.py`**: Se definieron los esquemas de datos utilizando Pydantic para las entidades `Producto` y `Pedido`, especificando sus atributos y tipos de datos.

## Clase 2: API REST y Swagger UI
- **Creación de `main.py`**: Se desarrolló la API REST en FastAPI, que incluye:
  - **CRUD de productos**: Endpoints para crear (`POST`), obtener todos (`GET`), obtener por ID (`GET`), actualizar (`PUT`) y eliminar (`DELETE`) productos.
  - **Registro de pedidos**: Endpoints para registrar (`POST`) y listar (`GET`) pedidos.
  - La conexión a la base de datos se importa directamente desde `database.py` de manera que el código original no ha sido modificado en lo absoluto.

## Gestión de Versiones en GitHub
- Se inicializó un repositorio local con `git init`.
- Se creó el archivo `.gitignore` para ignorar archivos sensibles como `.env`.
- Se realizaron los respectivos commits según las entregas de cada fase y se fusionaron a la rama `main`:
  1. `Primer commit con estructura, requirements.txt y modelos Pydantic.`
  2. `Merge a main con la API funcional y lista para ser consumida.`
