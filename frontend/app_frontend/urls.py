from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<str:id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<str:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/nuevo/', views.crear_pedido, name='crear_pedido'),
]
