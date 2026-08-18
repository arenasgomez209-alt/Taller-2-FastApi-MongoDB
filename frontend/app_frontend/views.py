import requests
from django.shortcuts import render, redirect
from django.conf import settings

API_URL = "http://127.0.0.1:8000"

def lista_productos(request):
    try:
        response = requests.get(f"{API_URL}/productos/")
        productos = response.json() if response.status_code == 200 else []
        for p in productos:
            p['id'] = p.pop('_id', None)
    except:
        productos = []
    return render(request, "app_frontend/lista_productos.html", {"productos": productos})

def crear_producto(request):
    if request.method == "POST":
        data = {
            "nombre": request.POST.get("nombre"),
            "descripcion": request.POST.get("descripcion"),
            "precio": float(request.POST.get("precio")),
            "stock": int(request.POST.get("stock")),
        }
        requests.post(f"{API_URL}/productos/", json=data)
        return redirect("lista_productos")
    return render(request, "app_frontend/formulario_producto.html")

def editar_producto(request, id):
    if request.method == "POST":
        data = {
            "nombre": request.POST.get("nombre"),
            "descripcion": request.POST.get("descripcion"),
            "precio": float(request.POST.get("precio")),
            "stock": int(request.POST.get("stock")),
        }
        requests.put(f"{API_URL}/productos/{id}", json=data)
        return redirect("lista_productos")
    
    try:
        response = requests.get(f"{API_URL}/productos/{id}")
        producto = response.json() if response.status_code == 200 else None
        if producto:
            producto['id'] = producto.pop('_id', None)
    except:
        producto = None
    return render(request, "app_frontend/formulario_producto.html", {"producto": producto})

def eliminar_producto(request, id):
    if request.method == "POST":
        requests.delete(f"{API_URL}/productos/{id}")
        return redirect("lista_productos")
    return render(request, "app_frontend/confirmar_eliminar.html", {"id": id})

def lista_pedidos(request):
    try:
        response = requests.get(f"{API_URL}/pedidos/")
        pedidos = response.json() if response.status_code == 200 else []
        for p in pedidos:
            p['id'] = p.pop('_id', None)
    except:
        pedidos = []
    return render(request, "app_frontend/lista_pedidos.html", {"pedidos": pedidos})

def crear_pedido(request):
    if request.method == "POST":
        productos_ids = request.POST.getlist("productos_ids")
        total = float(request.POST.get("total", 0))
        data = {
            "productos_ids": productos_ids,
            "total": total
        }
        requests.post(f"{API_URL}/pedidos/", json=data)
        return redirect("lista_pedidos")
    
    # Para el form, traemos los productos para poder seleccionarlos
    try:
        response = requests.get(f"{API_URL}/productos/")
        productos = response.json() if response.status_code == 200 else []
        for p in productos:
            p['id'] = p.pop('_id', None)
    except:
        productos = []
    return render(request, "app_frontend/formulario_pedido.html", {"productos": productos})
