from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from Usuarios.models import Usuario


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=25)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ManyToManyField(Categoria)
    descripcion = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return f"{self.nombre} "

class UserCarrito(models.Model):
    email = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'carrito'
        verbose_name_plural = 'carritos'

    def __str__(self):
        return f"Carrito de {self.usuario.email}"

class UserItemCarrito(models.Model):
    carrito = models.ForeignKey(UserCarrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario_id = models.IntegerField(default=0)
    cantidad = models.PositiveIntegerField(default=1)
    nombre_producto = models.CharField(max_length=100, default='Nombre Producto')
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imagen_producto = models.ImageField(upload_to='productos/', default='default.jpg')

    class Meta:
        verbose_name = 'elemento de carrito'
        verbose_name_plural = 'elementos de carrito'

    def __str__(self):
        return f"{self.cantidad}x {self.nombre_producto} en {self.carrito}"
