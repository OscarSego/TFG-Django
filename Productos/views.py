from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseServerError
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

def buscar_producto(request, nombre):
    try:
        producto = Producto.objects.get(nombre=nombre)
        serializer = ProductoSerializer(producto)
        return JsonResponse(serializer.data)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'El producto no existe'}, status=404)
    except Exception as e:
        return HttpResponseServerError({'error': 'Error interno del servidor: {}'.format(str(e))}, status=500)
