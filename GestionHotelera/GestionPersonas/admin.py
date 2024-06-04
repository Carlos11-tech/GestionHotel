from django.contrib import admin
from .models import Cliente, Personal, Reserva, CheckIn, CheckOut

# admin.site.register(Persona)  # Comentado porque Persona es un modelo abstracto
admin.site.register(Cliente)
admin.site.register(Personal)
admin.site.register(Reserva)
admin.site.register(CheckIn)
admin.site.register(CheckOut)