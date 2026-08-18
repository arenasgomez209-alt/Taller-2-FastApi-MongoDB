# 📋 Documentación de Cambios - Taller 2: FastAPI + MongoDB + Django

## 🎯 Resumen General
En este proyecto se integró una arquitectura desacoplada donde **FastAPI** actúa como backend API REST conectándose a una base de datos NoSQL (**MongoDB Atlas**), y **Django** actúa como capa de frontend web consumiendo dicha API mediante peticiones HTTP.

---

## 🛠️ Principales Cambios Realizados

### 1. 🍃 Migración y Exclusividad NoSQL (MongoDB Atlas)
- **Eliminación de SQL / SQLite**: Se removió el archivo `db.sqlite3` y todas las dependencias del ORM relacional de Django (`django.db.models`, `admin`, `auth`, `sessions`, `contenttypes`).
- **Base de Datos NoSQL**: Conexión configurada con `motor` / `pymongo` apuntando al clúster de MongoDB Atlas (`ambiente502`).
- **Configuración Dinámica (`.env`)**: Variables de entorno `MONGODB_URL` y `MONGODB_DB` para fácil parametrización.

### 2. ⚡ Backend FastAPI (`app/`)
- **Controlador Principal (`app/main.py`)**: Endpoints CRUD completos para `productos` y registro/consulta de `pedidos`.
- **Ruta Raíz (`/`)**: Endpoint de bienvenida y documentación rápida apuntando a `/docs`.
- **Manejo de ObjectIds**: Serialización automática de `_id` de MongoDB a cadenas legibles en JSON.

### 3. 🎨 Frontend Web Interactivo con Vanilla CSS (`frontend/`)
- **Sistema de Diseño Propio (`static/css/styles.css`)**:
  - Tipografía moderna con **Plus Jakarta Sans** (Google Fonts).
  - Paleta de colores índigo/violeta con efectos de elevación (*hover lifts*) y sombras suaves.
  - Indicador de estado con pulso animado para la conexión FastAPI + MongoDB.
- **Catálogo Interactivo de Productos**:
  - Tarjetas KPI con contadores en tiempo real (total de productos, stock acumulado, precio promedio).
  - Buscador instantáneo reactivo mientras se escribe (sin recargar la página).
  - Selector de ordenamiento dinámico (por precio o stock).
- **Selector Visual de Pedidos**:
  - Cuadrícula interactiva de productos seleccionables al clic con cálculo de total en vivo.
- **Formulario con Previsualización en Vivo**:
  - Al crear/editar productos, se renderiza una tarjeta de vista previa idéntica a la del catálogo.

### 4. 🛡️ Robustez y Manejo de Errores (`views.py`)
- Manejo seguro de `ConnectionError` en caso de que el backend esté temporalmente apagado, mostrando alertas claras al usuario en lugar de errores 500.

### 5. 🚀 Automatización de Arranque (`iniciar_proyecto.bat`)
- Script de un solo clic que levanta tanto el Backend FastAPI (`puerto 8000`) como el Frontend Django (`puerto 8080`) y abre automáticamente el navegador.

---

## 💻 Instrucciones de Ejecución

### Opción Rápida:
Doble clic en el archivo `iniciar_proyecto.bat`.

### Opción Manual:
```bash
# Terminal 1: Backend FastAPI
uvicorn app.main:app --reload --port 8000

# Terminal 2: Frontend Django
cd frontend
python manage.py runserver 8080
```

- **Frontend:** http://127.0.0.1:8080/
- **Swagger Docs:** http://127.0.0.1:8000/docs
