from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Producto(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int

class Pedido(BaseModel):
    productos_ids: List[str]
    total: float
    fecha: datetime = Field(default_factory=datetime.now)
