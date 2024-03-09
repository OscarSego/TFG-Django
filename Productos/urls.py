from django.urls import path
from . import views

urlpatterns = [
    path('producto/', views.get_producto, name='get_producto'),
    path('producto/<int:producto_id>/', views.buscar_producto, name='buscar_producto')
]