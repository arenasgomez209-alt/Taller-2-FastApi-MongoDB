import os
import re
import requests
from django.shortcuts import render, redirect

def get_api_url():
    """Obtiene y limpia la URL de la API eliminando formato markdown accidental o barras finales."""
    raw_url = os.getenv("API_URL", "http://127.0.0.1:8000").strip()
    match = re.search(r'https?://[^\s\)\]]+', raw_url)
    if match:
        url = match.group(0)
    else:
        url = raw_url
    return url.rstrip("/")


def lista_productos(request):
    error = None
    api_url = get_api_url()
    try:
        response = requests.get(f"{api_url}/productos/", timeout=5)
        productos = response.json() if response.status_code == 200 else []
        for p in productos:
            p['id'] = p.pop('_id', None)
    except requests.exceptions.ConnectionError:
        productos = []
        error = f"No se pudo conectar con el Backend (FastAPI en {api_url}). Asegúrate de que esté encendido."
    except Exception as e:
        productos = []
        error = f"Error inesperado: {str(e)}"
    return render(request, "app_frontend/lista_productos.html", {"productos": productos, "error": error})


def crear_producto(request):
    error = None
    api_url = get_api_url()
    if request.method == "POST":
        data = {
            "nombre": request.POST.get("nombre"),
            "descripcion": request.POST.get("descripcion"),
            "precio": float(request.POST.get("precio", 0)),
            "stock": int(request.POST.get("stock", 0)),
        }
        try:
            res = requests.post(f"{api_url}/productos/", json=data, timeout=5)
            if res.status_code in (200, 201):
                return redirect("lista_productos")
            else:
                error = f"Error al guardar producto: {res.text}"
        except requests.exceptions.ConnectionError:
            error = f"No se pudo conectar con el Backend (FastAPI en {api_url}). Comprueba que esté corriendo."
        except Exception as e:
            error = f"Error al crear producto: {str(e)}"
            
    return render(request, "app_frontend/formulario_producto.html", {"error": error})


def editar_producto(request, id):
    error = None
    api_url = get_api_url()
    if request.method == "POST":
        data = {
            "nombre": request.POST.get("nombre"),
            "descripcion": request.POST.get("descripcion"),
            "precio": float(request.POST.get("precio", 0)),
            "stock": int(request.POST.get("stock", 0)),
        }
        try:
            res = requests.put(f"{api_url}/productos/{id}", json=data, timeout=5)
            if res.status_code == 200:
                return redirect("lista_productos")
            else:
                error = f"Error al actualizar producto: {res.text}"
        except requests.exceptions.ConnectionError:
            error = f"No se pudo conectar con el Backend (FastAPI en {api_url})."
        except Exception as e:
            error = f"Error: {str(e)}"
    
    producto = None
    try:
        response = requests.get(f"{api_url}/productos/{id}", timeout=5)
        producto = response.json() if response.status_code == 200 else None
        if producto:
            producto['id'] = producto.pop('_id', None)
    except requests.exceptions.ConnectionError:
        error = f"No se pudo conectar con el Backend (FastAPI en {api_url})."
    except Exception:
        producto = None

    return render(request, "app_frontend/formulario_producto.html", {"producto": producto, "error": error})


def eliminar_producto(request, id):
    error = None
    api_url = get_api_url()
    if request.method == "POST":
        try:
            res = requests.delete(f"{api_url}/productos/{id}", timeout=5)
            if res.status_code == 200:
                return redirect("lista_productos")
            else:
                error = f"Error al eliminar: {res.text}"
        except requests.exceptions.ConnectionError:
            error = f"No se pudo conectar con el Backend (FastAPI en {api_url})."
        except Exception as e:
            error = str(e)
    return render(request, "app_frontend/confirmar_eliminar.html", {"id": id, "error": error})


def lista_pedidos(request):
    error = None
    api_url = get_api_url()
    try:
        response = requests.get(f"{api_url}/pedidos/", timeout=5)
        pedidos = response.json() if response.status_code == 200 else []
        for p in pedidos:
            p['id'] = p.pop('_id', None)
    except requests.exceptions.ConnectionError:
        pedidos = []
        error = f"No se pudo conectar con el Backend (FastAPI en {api_url})."
    except Exception as e:
        pedidos = []
        error = str(e)
    return render(request, "app_frontend/lista_pedidos.html", {"pedidos": pedidos, "error": error})


def crear_pedido(request):
    error = None
    api_url = get_api_url()
    if request.method == "POST":
        productos_ids = request.POST.getlist("productos_ids")
        total = float(request.POST.get("total", 0))
        data = {
            "productos_ids": productos_ids,
            "total": total
        }
        try:
            res = requests.post(f"{api_url}/pedidos/", json=data, timeout=5)
            if res.status_code in (200, 201):
                return redirect("lista_pedidos")
            else:
                error = f"Error al crear pedido: {res.text}"
        except requests.exceptions.ConnectionError:
            error = f"No se pudo conectar con el Backend (FastAPI en {api_url})."
        except Exception as e:
            error = str(e)
    
    productos = []
    try:
        response = requests.get(f"{api_url}/productos/", timeout=30)
        productos = response.json() if response.status_code == 200 else []
        for p in productos:
            p['id'] = p.pop('_id', None)
    except requests.exceptions.ConnectionError:
        error = f"No se pudo cargar la lista de productos porque FastAPI ({api_url}) no está respondiendo."
    except Exception:
        productos = []

    return render(request, "app_frontend/formulario_pedido.html", {"productos": productos, "error": error})
