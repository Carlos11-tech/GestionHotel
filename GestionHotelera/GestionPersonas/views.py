from django.shortcuts import render

def pagina_inicio(request):
    return render(request, 'pagina_inicio.html')

def ver_servicios(request):
    # Lógica para mostrar los servicios disponibles
    return render(request, 'ver_servicios.html')

def ver_tipos_habitaciones(request):
    # Lógica para mostrar los tipos de habitaciones disponibles
    return render(request, 'ver_tipos_habitaciones.html')

def reserva_habitacion(request):
    # Lógica para reservar una habitación
    return render(request, 'reserva_habitacion.html')

def registrar_cliente(request):
    # Lógica para registrar un cliente
    return render(request, 'registrar_cliente.html')
