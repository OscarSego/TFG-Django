from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'precio', 'categorias')

    def categorias(self, obj):
        return ", ".join([c.nombre for c in obj.categoria.all()])

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
