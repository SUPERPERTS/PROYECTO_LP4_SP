from django.contrib import admin
from .models import Link

# Register your models here.
@admin.register(Link)
class linkAdmin(admin.ModelAdmin):
    '''Admin View for link'''

    def get_readonly_fields(self, request, obj=None): #? Llamndo al metodo para mostrar los campo solo de lectura de una forma especial
        if request.user.groups.filter(name="Personal").exists():
        #? Si dentro del usuario pertenece al grupo "Personal" entonces...
            return ('name', 'key')
            #? Si es un usuario normal tendra un acceso limitado y tendra 4 campos solo de lectura
        else:
            #? Si es un superusuario entonces podra modificar mas campos en este caso 'key' y 'name'
            return ('created', 'updated')