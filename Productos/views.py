from django.http import JsonResponse
from .models import Producto
from django.shortcuts import get_object_or_404
from .serializers import ProductoSerializer

# Create your views here.
def get_producto(request):
    try:
        productos = Producto.objects.all()
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)

    serializer = ProductoSerializer(productos, many=True)
    return JsonResponse(serializer.data, safe=False)

def buscar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    serializer = ProductoSerializer(producto)
    return JsonResponse(serializer.data)
