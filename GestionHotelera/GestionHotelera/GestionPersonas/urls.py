from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('ver_servicios/', views.ver_servicios, name='ver_servicios'),
    path('ver_tipos_habitaciones/', views.ver_tipos_habitaciones, name='ver_tipos_habitaciones'),
    path('reserva_habitacion/', views.reserva_habitacion, name='reserva_habitacion'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),

]
