from django.urls import path
from .views import pagina_inicio, ver_servicios, ver_tipos_habitaciones, crear_reserva, registrar_cliente, reserva_exitosa

urlpatterns = [
    path('', pagina_inicio, name='pagina_inicio'),
    path('ver_servicios/', ver_servicios, name='ver_servicios'),
    path('ver_tipos_habitaciones/', ver_tipos_habitaciones, name='ver_tipos_habitaciones'),
    path('crear_reserva/', crear_reserva, name='crear_reserva'),
    path('registrar_cliente/', registrar_cliente, name='registrar_cliente'),
    path('reserva_exitosa/', reserva_exitosa, name='reserva_exitosa'),
]

