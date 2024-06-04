from django.contrib import admin
from .models import Empleado, Contratar, Administrador, GestionarEmpleado

admin.site.register(Empleado)
admin.site.register(Contratar)
admin.site.register(Administrador)
admin.site.register(GestionarEmpleado)