from django.urls import path
from . import views

urlpatterns = [
    path('producto', views.get_producto, name='get_producto'),
    path('producto/nombre/<str:nombre>', views.buscar_producto, name='buscar_producto'),
    path('producto/agregar-al-carrito/<int:producto_id>', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('producto/visualizar-carrito', views.visualizar_carrito, name='visualizar_carrito'),
]