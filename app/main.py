import sys
import os
from pathlib import Path

# Añadir rutas a sys.path para compatibilidad con despliegues en Render y local
BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from fastapi import FastAPI, HTTPException
try:
    from app.models.schemas import Producto, Pedido
    from app.core.database import database
except (ImportError, ModuleNotFoundError):
    from models.schemas import Producto, Pedido
    from core.database import database

from bson import ObjectId
from typing import List

app = FastAPI(title="API REST - Clase 2", description="CRUD de productos y registro de pedidos")

productos_collection = database.productos
pedidos_collection = database.pedidos

@app.get("/", tags=["General"])
async def inicio():
    return {
        "mensaje": "API FastAPI con MongoDB activa y funcionando",
        "documentacion": "/docs",
        "productos": "/productos/",
        "pedidos": "/pedidos/"
    }

# Helper function para convertir ObjectId a str
def serialize_doc(doc):
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc

# ===============================
# CRUD DE PRODUCTOS
# ===============================

@app.post("/productos/", tags=["Productos"])
async def crear_producto(producto: Producto):
    nuevo_producto = await productos_collection.insert_one(producto.model_dump())
    producto_creado = await productos_collection.find_one({"_id": nuevo_producto.inserted_id})
    return serialize_doc(producto_creado)

@app.get("/productos/", tags=["Productos"])
async def obtener_productos():
    productos = await productos_collection.find().to_list(100)
    return [serialize_doc(p) for p in productos]

@app.get("/productos/{id}", tags=["Productos"])
async def obtener_producto(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    producto = await productos_collection.find_one({"_id": ObjectId(id)})
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return serialize_doc(producto)

@app.put("/productos/{id}", tags=["Productos"])
async def actualizar_producto(id: str, producto: Producto):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    resultado = await productos_collection.update_one({"_id": ObjectId(id)}, {"$set": producto.model_dump()})
    if resultado.matched_count == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    producto_actualizado = await productos_collection.find_one({"_id": ObjectId(id)})
    return serialize_doc(producto_actualizado)

@app.delete("/productos/{id}", tags=["Productos"])
async def eliminar_producto(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    resultado = await productos_collection.delete_one({"_id": ObjectId(id)})
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado exitosamente"}

# ===============================
# REGISTRO DE PEDIDOS
# ===============================

@app.post("/pedidos/", tags=["Pedidos"])
async def registrar_pedido(pedido: Pedido):
    if not pedido.productos_ids:
        raise HTTPException(status_code=400, detail="El pedido debe contener al menos un producto.")
    
    # Validar existencia y stock de cada producto
    for prod_id in pedido.productos_ids:
        if not ObjectId.is_valid(prod_id):
            raise HTTPException(status_code=400, detail=f"ID de producto inválido: {prod_id}")
        
        producto = await productos_collection.find_one({"_id": ObjectId(prod_id)})
        if not producto:
            raise HTTPException(status_code=404, detail=f"Producto con ID {prod_id} no encontrado.")
        
        if producto.get("stock", 0) <= 0:
            raise HTTPException(
                status_code=400, 
                detail=f"El producto '{producto.get('nombre')}' no tiene stock disponible (Agotado)."
            )
        
        # Descontar 1 unidad del stock en MongoDB
        await productos_collection.update_one(
            {"_id": ObjectId(prod_id)},
            {"$inc": {"stock": -1}}
        )

    nuevo_pedido = await pedidos_collection.insert_one(pedido.model_dump())
    pedido_creado = await pedidos_collection.find_one({"_id": nuevo_pedido.inserted_id})
    return serialize_doc(pedido_creado)

@app.get("/pedidos/", tags=["Pedidos"])
async def obtener_pedidos():
    pedidos = await pedidos_collection.find().to_list(100)
    return [serialize_doc(p) for p in pedidos]

