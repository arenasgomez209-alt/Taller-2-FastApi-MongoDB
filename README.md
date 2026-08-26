# 📦 Taller 2: Sistema de Gestión de Productos y Pedidos
> **Arquitectura Moderna:** Backend en **FastAPI** + Base de datos en la nube **MongoDB Atlas** + Frontend en **Django** con Catálogo Interactivo.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas_Motor-47A248.svg)](https://www.mongodb.com/atlas)
[![Django](https://img.shields.io/badge/Django-5.0%2B-092E20.svg)](https://www.djangoproject.com/)
[![Render](https://img.shields.io/badge/Deploy-Render-46E3B7.svg)](https://render.com)
[![Status](https://img.shields.io/badge/Release-v1.0-success.svg)]()

---

## 🌐 Enlaces de Despliegue en Vivo (Render)

| Servicio | Componente | Enlace de Acceso |
| :--- | :--- | :--- |
| 💻 **Aplicativo Web** | Frontend (Django) | 🔗 [https://taller-2-fastapi-mongodb-2.onrender.com](https://taller-2-fastapi-mongodb-2.onrender.com) |
| ⚡ **Backend API** | Backend (FastAPI) | 🔗 [https://taller-2-fastapi-mongodb-1.onrender.com](https://taller-2-fastapi-mongodb-1.onrender.com) |
| 📑 **Documentación Swagger** | Swagger UI | 🔗 [https://taller-2-fastapi-mongodb-1.onrender.com/docs](https://taller-2-fastapi-mongodb-1.onrender.com/docs) |
| 📖 **Documentación Redoc** | Redoc | 🔗 [https://taller-2-fastapi-mongodb-1.onrender.com/redoc](https://taller-2-fastapi-mongodb-1.onrender.com/redoc) |

---

## 📖 Descripción del Proyecto

Este proyecto implementa una solución desacoplada y escalable para la gestión integral de un catálogo de productos y el registro de órdenes de compra. 

Consta de:
- **Backend (FastAPI):** Expone una API REST asíncrona conectada mediante `motor` a un clúster de **MongoDB Atlas**, con validación de esquemas vía **Pydantic** y documentación OpenAPI/Swagger automática.
- **Frontend (Django):** Aplicación web que consume la API REST de FastAPI mediante `requests`, proveyendo una interfaz interactiva estilo SaaS para el catálogo, creación/edición en tiempo real, control de stock y gestión de pedidos.

---

## 🌟 Características Principales

- ⚡ **API REST Asíncrona (FastAPI):** Endpoints para CRUD completo de productos y registro de pedidos con serialización de `ObjectId`.
- 🗄️ **Persistencia NoSQL (MongoDB Atlas):** Almacenamiento seguro en la nube en colecciones `productos` y `pedidos`.
- 📊 **Catálogo Interactivo:**
  - Métricas KPI en tiempo real (Total de productos, stock acumulado, precio promedio y valor estimado del inventario).
  - Buscador instantáneo sin recarga de página por nombre y descripción.
  - Filtro por píldoras (*Todos*, *En Stock*, *Stock Bajo*, *Agotados*).
  - Ordenamiento multidimensional (precio, mayor stock, orden alfabético).
  - Selector de vista: Cuadrícula (*Cards*) o Lista (*Compacta*).
  - Modal de **Vista Rápida (Quick View)** para inspección detallada.
- 👁️ **Formularios con Vista Previa en Vivo:** Tarjeta interactiva 3D que previsualiza los cambios al instante mientras el usuario escribe.
- 🛒 **Selector Visual de Pedidos:** Tarjetas dinámicas que calculan automáticamente el total a pagar y descuentan el stock en MongoDB al confirmar la orden.
- 🛡️ **Manejo Robusto de Excepciones:**
  - Control de fallos de conexión (API caída o inalcanzable) con avisos amigables al usuario.
  - Validación de stock disponible (bloqueo en frontend y rechazo en backend si un producto está agotado).
  - Validación de identificadores `ObjectId` de MongoDB.

---

## 🛠️ Tecnologías y Librerías

| Componente | Tecnología / Librería | Propósito |
| :--- | :--- | :--- |
| **Backend** | `FastAPI`, `Uvicorn` | API REST asíncrona de alto rendimiento |
| **ODM / Base de Datos** | `Motor`, `PyMongo`, `MongoDB Atlas` | Conductor asíncrono hacia base de datos NoSQL |
| **Validación de Datos** | `Pydantic`, `Pydantic-Settings` | Tipado estricto y serialización |
| **Frontend** | `Django` | Servidor web y motor de plantillas |
| **Consumo HTTP** | `Requests` | Cliente HTTP síncrono para comunicarse con la API |
| **Estilos e Interfaz** | `Vanilla CSS3`, `Plus Jakarta Sans` | Sistema de diseño moderno, micro-animaciones y glassmorphism |
| **Configuración** | `python-dotenv` | Gestión segura de variables de entorno |

---

## 📂 Estructura del Proyecto

```text
Taller2FastAPI/
├── app/                            # Backend FastAPI
│   ├── core/
│   │   ├── __init__.py
│   │   └── database.py             # Conexión a MongoDB Atlas con Motor
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py              # Modelos Pydantic (Producto, Pedido)
│   ├── __init__.py
│   ├── main.py                     # API REST, endpoints CRUD y pedidos
│   └── requirements.txt            # Dependencias del proyecto
│
├── frontend/                       # Frontend Django
│   ├── app_frontend/
│   │   ├── static/
│   │   │   └── css/
│   │   │       └── styles.css      # Sistema de diseño y animaciones CSS
│   │   ├── templates/
│   │   │   └── app_frontend/
│   │   │       ├── base.html              # Plantilla base y notificaciones Toast
│   │   │       ├── lista_productos.html   # Catálogo y KPIs
│   │   │       ├── formulario_producto.html# Crear/Editar con Live Preview
│   │   │       ├── lista_pedidos.html     # Historial de pedidos
│   │   │       ├── formulario_pedido.html # Selector de pedidos interactivo
│   │   │       └── confirmar_eliminar.html# Diálogo de confirmación
│   │   ├── views.py                # Lógica de consumo de la API con Requests
│   │   └── urls.py                 # Enrutamiento de vistas de Django
│   ├── config/                     # Configuración principal de Django
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
│
├── .env                            # Variables de entorno (Credenciales MongoDB)
├── .gitignore
├── iniciar_proyecto.bat            # Script de arranque automático en 1 clic
└── README.md                       # Documentación técnica
```

---

## ⚙️ Configuración Inicial

### 1. Clonar el repositorio y crear el entorno virtual
```bash
git clone https://github.com/arenasgomez209-alt/Taller-2-FastApi-MongoDB.git
cd Taller-2-FastApi-MongoDB

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual en Windows
.venv\Scripts\activate
```

### 2. Instalar dependencias
```bash
pip install -r app/requirements.txt
```

### 3. Configurar variables de entorno (`.env`)
Crea un archivo `.env` en la raíz del proyecto con tus credenciales de MongoDB Atlas:
```env
MONGODB_URL=mongodb+srv://<usuario>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
MONGODB_DB=ambiente502
```

> **Nota de Seguridad en MongoDB Atlas:** Recuerda autorizar tu dirección IP en **Network Access** (`0.0.0.0/0` o tu IP actual) dentro de MongoDB Atlas para permitir el tráfico SSL/TLS.

---

## 🚀 Ejecución del Proyecto

### Opción A: Modo Automático (Recomendado)
Ejecuta el archivo [iniciar_proyecto.bat](file:///c:/Users/nikol/Desktop/Taller2FastAPI/iniciar_proyecto.bat):
```cmd
iniciar_proyecto.bat
```
*Este script activará `.venv`, levantará FastAPI en el puerto 8000, Django en el puerto 8080 y abrirá el navegador automáticamente.*

---

### Opción B: Modo Manual (2 Terminales)

#### Terminal 1 — Backend (FastAPI):
```bash
.venv\Scripts\activate
uvicorn app.main:app --reload --port 8000
```
- **Documentación Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Documentación Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

#### Terminal 2 — Frontend (Django):
```bash
.venv\Scripts\activate
cd frontend
python manage.py runserver 8080
```
- **Aplicación Web:** [http://127.0.0.1:8080/](http://127.0.0.1:8080/)

---

## 📡 Endpoints de la API REST

| Método | Endpoint | Descripción | Parámetros / Body |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Estado general del servicio API | - |
| `GET` | `/productos/` | Obtiene la lista de todos los productos | - |
| `POST` | `/productos/` | Crea un nuevo producto en MongoDB | `Producto` (nombre, descripción, precio, stock) |
| `GET` | `/productos/{id}` | Obtiene un producto por su `_id` | `id` (ObjectId) |
| `PUT` | `/productos/{id}` | Actualiza un producto existente | `id` (ObjectId), `Producto` |
| `DELETE` | `/productos/{id}` | Elimina un producto de MongoDB | `id` (ObjectId) |
| `GET` | `/pedidos/` | Lista todos los pedidos registrados | - |
| `POST` | `/pedidos/` | Valida stock y registra un pedido | `Pedido` (productos_ids, total, fecha) |

---

## 🛡️ Manejo de Excepciones y Casos Límite

1. **API Inaccesible o Caída:** Si el backend FastAPI se encuentra detenido o no responde, el frontend en Django captura `requests.exceptions.ConnectionError` y `requests.exceptions.Timeout`, mostrando un banner de aviso preventivo en lugar de una pantalla de error del servidor (500).
2. **Control de Stock en Pedidos:**
   - En el **Frontend**, los productos agotados (`stock = 0`) aparecen deshabilitados con la etiqueta `Sin Stock (Agotado)` y no pueden ser seleccionados.
   - En el **Backend**, el endpoint `POST /pedidos/` verifica que cada producto tenga `stock > 0`. Si no hay existencias, retorna un error `HTTP 400 Bad Request` indicando el nombre del producto agotado.
   - Al registrarse exitosamente un pedido, el backend descuenta automáticamente 1 unidad del stock de cada producto en MongoDB (`$inc: { stock: -1 }`).
3. **IDs no válidos en MongoDB:** Se verifica con `ObjectId.is_valid(id)` antes de realizar consultas para evitar excepciones no controladas de `BSONTypeError`.

---

## 👥 Entrega y Release
- **Versión:** `v1.0`
- **Taller:** Taller 2 - FastAPI + MongoDB + Django
