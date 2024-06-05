"""
URL configuration for GestionHotelera project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GestionPersonas import views
from GestionPersonas.views import crear_reserva, reserva_exitosa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('ver_servicios/', views.ver_servicios, name='ver_servicios'),
    path('ver_tipos_habitaciones/', views.ver_tipos_habitaciones, name='ver_tipos_habitaciones'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('crear_reserva/', crear_reserva, name='crear_reserva'),
    path('reserva_exitosa/', reserva_exitosa, name='reserva_exitosa'),
]
