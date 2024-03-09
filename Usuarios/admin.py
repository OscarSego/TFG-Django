from django.contrib import admin
from .models import Role, Usuario

# Register your models here.

class RoleAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('email', 'roles_list')

    def roles_list(self, obj):
        return ", ".join([role.role for role in obj.role.all()])

admin.site.register(Role, RoleAdmin)
admin.site.register(Usuario, UsuarioAdmin)
