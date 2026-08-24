# Taller 2: FastAPI + MongoDB + Django

Proyecto con backend en FastAPI conectado a MongoDB Atlas y frontend en Django que consume la API para gestionar productos y pedidos.

## Clase 4 - Templates y Catálogo en Django
- Creación de las plantillas HTML (`base.html`, `lista_productos.html`, formularios).
- Uso de template tags de Django (`{% for %}`, `{% if %}`, `{{ ... }}`) para iterar y mostrar los productos obtenidos desde la API.
- Interfaz del catálogo terminada y estilizada con CSS.

## Ejecución del proyecto

1. **Backend (FastAPI):**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
   - Swagger docs: http://127.0.0.1:8000/docs

2. **Frontend (Django):**
   ```bash
   cd frontend
   python manage.py runserver 8080
   ```
   - Panel web: http://127.0.0.1:8080/
