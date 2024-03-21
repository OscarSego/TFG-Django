from django.urls import path
from . import views

urlpatterns = [
    path('producto', views.get_producto, name='get_producto'),
    path('producto/nombre/<str:nombre>', views.buscar_producto, name='buscar_producto'),
    path('producto/agregar-al-carrito/<int:producto_id>', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('producto/visualizar-carrito', views.visualizar_carrito, name='visualizar_carrito'),
    path('producto/aumentar-cantidad/<int:producto_id>', views.aumentar_cantidad_producto, name='aumentar_cantidad_producto'),
    path('producto/disminuir-cantidad/<int:producto_id>', views.restar_producto_carrito, name='restar_producto_carrito'),
    path('producto/borrar-carrito', views.borrar_carrito, name='borrar_carrito'),
]