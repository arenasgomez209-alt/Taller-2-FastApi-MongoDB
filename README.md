# 🚀 Taller 2: FastAPI + MongoDB + Django Frontend

Proyecto de desarrollo web con arquitectura desacoplada, utilizando **FastAPI** con **MongoDB Atlas** en el Backend y **Django** en el Frontend consumiendo la API REST.

---

## 📌 Bitácora de Desarrollo

### 🔹 Clase 4 — Django: Templates y Catálogo
* **Construcción de Plantillas HTML:** Creación y estructuración de la interfaz del Frontend (`base.html`, `lista_productos.html`, `formulario_producto.html`, `lista_pedidos.html`, `formulario_pedido.html`).
* **Uso de Django Template Tags:** Implementación de etiquetas de plantilla (`{% for %}`, `{% if %}`, `{% empty %}`, `{% url %}`) para iterar sobre los datos provenientes de la API de FastAPI y renderizar el catálogo de productos de forma visual y dinámica.
* **Interfaz Gráfica del Catálogo:** Diseño visual completo con Vanilla CSS, tarjetas de métricas/KPIs en tiempo real, barra de búsqueda reactiva y filtros interactivos.
* **Integración API REST:** Conexión desde las vistas de Django (`views.py`) hacia el backend FastAPI mediante peticiones HTTP con la librería `requests`.

---

## 🏗️ Arquitectura del Proyecto

```text
Taller2FastAPI/
├── app/                        # Backend (FastAPI + MongoDB)
│   ├── core/
│   │   └── database.py         # Conexión a MongoDB Atlas
│   ├── models/
│   │   └── schemas.py          # Modelos Pydantic para validación
│   └── main.py                 # API REST (Endpoints CRUD de productos y pedidos)
├── frontend/                   # Frontend (Django)
│   ├── app_frontend/
│   │   ├── templates/app_frontend/
│   │   │   ├── base.html       # Plantilla base con navbar y estilos globales
│   │   │   ├── lista_productos.html # Catálogo de productos (Clase 4)
│   │   │   ├── formulario_producto.html
│   │   │   ├── lista_pedidos.html
│   │   │   └── formulario_pedido.html
│   │   ├── static/css/
│   │   │   └── styles.css      # Sistema de diseño con Vanilla CSS
│   │   ├── views.py            # Vistas que consumen la API de FastAPI
│   │   └── urls.py             # Enrutamiento del frontend
│   └── config/                 # Configuración de Django
├── iniciar_proyecto.bat        # Script de ejecución rápida
└── README.md                   # Documentación del proyecto
```

---

## ⚙️ Instrucciones de Ejecución

### Opción 1: Ejecución Automática (Windows)
Ejecutar el archivo `iniciar_proyecto.bat` haciendo doble clic sobre él.

### Opción 2: Ejecución Manual

1. **Activar el entorno virtual:**
   ```bash
   .venv\Scripts\activate
   ```

2. **Iniciar el Backend (FastAPI):**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
   * *Swagger UI / Documentación:* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

3. **Iniciar el Frontend (Django):**
   ```bash
   cd frontend
   python manage.py runserver 8080
   ```
   * *Catálogo Web:* [http://127.0.0.1:8080/](http://127.0.0.1:8080/)
