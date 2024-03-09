from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    role = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'role'
        verbose_name_plural = 'roles'

    def __str__(self):
        return self.role

class Usuario(models.Model):
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=150)
    role = models.ManyToManyField(Role)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return f"{self.email} "

class UsuarioRole(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        db_table = 'usuarios_usuario_role'

