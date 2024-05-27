import logging
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from rest_framework.utils import json

# Configurar el registro
logger = logging.getLogger(__name__)
# Funcion para enviar correos
def enviar_correo(request):
    # Verificar si la solicitud es de tipo POST
    if request.method == 'POST':
        # Obtener los datos del cuerpo de la solicitud POST
        data = json.loads(request.body)
        nombre = data.get('nombre')
        correo = data.get('correo')
        mensaje = data.get('mensaje')

        # Definir el destinatario, asunto y cuerpo del correo
        destinatario = 'lamparasoporto@gmail.com'
        asunto = f'Nuevo mensaje de contacto de {nombre}'
        cuerpo = f'Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}'

        try:
            # Enviar el correo electrónico
            send_mail(
                asunto,
                cuerpo,
                correo,  # Utilizar la dirección de correo proporcionada por el usuario como remitente
                [destinatario],
                fail_silently=False,
            )
            # Registrar el envío exitoso del correo electrónico
            logger.info('Correo electrónico enviado correctamente: %s', asunto)
            # Devolver una respuesta JSON indicando que el correo se envió correctamente
            return JsonResponse({'mensaje': 'Correo enviado correctamente'})
        except Exception as e:
            # Manejar errores en caso de que falle el envío del correo
            logger.error('Error al enviar el correo electrónico: %s', str(e))
            # Devolver una respuesta JSON indicando que ocurrió un error al enviar el correo
            return JsonResponse({'error': 'Error al enviar el correo electrónico'}, status=500)
    else:
        # Manejar solicitudes que no son de tipo POST
        logger.error('La solicitud debe ser de tipo POST')
        # Devolver una respuesta JSON indicando que la solicitud debe ser de tipo POST
        return JsonResponse({'error': 'La solicitud debe ser de tipo POST'})