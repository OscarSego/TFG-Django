from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseServerError
from .models import Producto, UserCarrito, UserItemCarrito
from django.shortcuts import get_object_or_404
from .serializers import ProductoSerializer, CarritoSerializer
import jwt
from django.conf import settings
import logging


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

def eliminar_producto_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return JsonResponse({'mensaje': 'Producto eliminado del carrito correctamente'})

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def agregar_al_carrito(request, producto_id):
    try:
        # Obtener el token de autorización del encabezado de la solicitud
        token = request.headers.get('authorization')
        logger.info('Token de autorización recibido: %s', token)
        if not token or not token.startswith('Bearer '):
            logger.error('Token de autorización inválido')
            return JsonResponse({'mensaje': 'Token de autorización inválido'}, status=401)

        token_parts = token.split(' ')
        if len(token_parts) != 2:
            logger.error('Token de autorización inválido')
            return JsonResponse({'mensaje': 'Token de autorización inválido'}, status=401)

        # Obtener el token real
        token_real = token_parts[1]

        # Decodificar y validar el token
        decoded_token = jwt.decode(token_real, settings.SECRET_KEY, algorithms=['HS256'])
        logger.info('Token decodificado: %s', decoded_token)

        # Extraer el ID de usuario del token (si el token contiene esta información)
        email_id = decoded_token.get('userId')
        logger.info('Id user: %s', email_id)
        if not email_id:
            logger.error('ID de usuario no encontrado en el token')
            return JsonResponse({'mensaje': 'ID de usuario no encontrado en el token'}, status=401)

        # Obtener el usuario actual
        usuario = email_id

        # Obtener o crear el carrito del usuario
        carrito, creado = UserCarrito.objects.get_or_create(email=usuario)

        # Verificar si el producto ya está en el carrito
        producto_carrito = UserItemCarrito.objects.filter(carrito=carrito, producto__id=producto_id).first()
        if producto_carrito:
            # El producto ya está en el carrito, aumentar la cantidad en 1
            producto_carrito.cantidad += 1
            producto_carrito.save()
            logger.info('Cantidad del producto incrementada en el carrito')
            return JsonResponse({'mensaje': 'Cantidad del producto incrementada en el carrito'})
        else:
            # Si el producto no está en el carrito, agregarlo con cantidad 1
            producto = get_object_or_404(Producto, pk=producto_id)
            item_carrito = UserItemCarrito.objects.create(
                carrito=carrito,
                producto=producto,
                usuario_id=email_id,
                cantidad=1,
                nombre_producto=producto.nombre,
                precio_producto=producto.precio,
                imagen_producto=producto.imagen
            )
            logger.info('Producto agregado al carrito correctamente')
            return JsonResponse({'mensaje': 'Producto agregado al carrito correctamente'})
    except jwt.ExpiredSignatureError:
        logger.error('Token de autorización expirado')
        return JsonResponse({'mensaje': 'Token de autorización expirado'}, status=401)

def visualizar_carrito(request):
    try:
        # Obtener el token de autorización del encabezado de la solicitud
        token = request.headers.get('authorization')
        if not token or not token.startswith('Bearer '):
            return JsonResponse({'error': 'Token de autorización inválido'}, status=401)

        token_parts = token.split(' ')
        if len(token_parts) != 2:
            return JsonResponse({'error': 'Token de autorización inválido'}, status=401)

        # Obtener el token real
        token_real = token_parts[1]

        # Decodificar y validar el token
        decoded_token = jwt.decode(token_real, settings.SECRET_KEY, algorithms=['HS256'])

        # Obtener el ID del usuario del token
        usuario_id = decoded_token.get('userId')
        if not usuario_id:
            return JsonResponse({'error': 'ID de usuario no encontrado en el token'}, status=401)

        # Obtener todos los elementos del carrito para el usuario actual
        elementos_carrito = UserItemCarrito.objects.filter(usuario_id=usuario_id)

        # Crear una lista de diccionarios con los datos de los elementos del carrito
        carrito_data = []
        for elemento in elementos_carrito:
            # Obtener el producto asociado al elemento del carrito
            producto = elemento.producto

            # Verificar si el producto tiene una imagen asociada
            if producto.imagen:
                imagen_url = request.build_absolute_uri(producto.imagen.url)
            else:
                imagen_url = None

            carrito_data.append({
                'nombre_producto': elemento.nombre_producto,
                'precio_producto': float(elemento.precio_producto),
                'imagen_producto': imagen_url,
                'cantidad': elemento.cantidad
            })

        # Devolver los datos del carrito en formato JSON
        return JsonResponse(carrito_data, safe=False)
    except jwt.ExpiredSignatureError:
        return JsonResponse({'error': 'Token de autorización expirado'}, status=401)
    except jwt.DecodeError:
        return JsonResponse({'error': 'Error al decodificar el token'}, status=401)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

