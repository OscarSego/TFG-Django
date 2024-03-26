import logging
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from rest_framework.utils import json

# Configurar el registro
logger = logging.getLogger(__name__)
def enviar_correo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data.get('nombre')
        correo = data.get('correo')
        mensaje = data.get('mensaje')

        destinatario = 'lamparasoporto@gmail.com'
        asunto = f'Nuevo mensaje de contacto de {nombre}'
        cuerpo = f'Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}'

        try:
            send_mail(
                asunto,
                cuerpo,
                correo,  # Utilizar la dirección de correo proporcionada por el usuario como remitente
                [destinatario],
                fail_silently=False,
            )
            logger.info('Correo electrónico enviado correctamente: %s', asunto)
            return JsonResponse({'mensaje': 'Correo enviado correctamente'})
        except Exception as e:
            logger.error('Error al enviar el correo electrónico: %s', str(e))
            return JsonResponse({'error': 'Error al enviar el correo electrónico'}, status=500)
    else:
        logger.error('La solicitud debe ser de tipo POST')
        return JsonResponse({'error': 'La solicitud debe ser de tipo POST'})