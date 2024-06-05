from django.shortcuts import render, redirect
from .forms import ReservaForm, ClienteForm

from .models import Cliente, Reserva


def pagina_inicio(request):
    return render(request, 'pagina_inicio.html')


def ver_servicios(request):
    return render(request, 'ver_servicios.html')


def ver_tipos_habitaciones(request):
    return render(request, 'ver_tipos_habitaciones.html')

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save()
            return redirect('reserva_exitosa')
    else:
        form = ReservaForm()
    return render(request, 'crear_reserva.html', {'form': form})


def reserva_exitosa(request):
    return render(request, 'reserva_exitosa.html')

from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el cliente en la base de datos
            return redirect('crear_reserva')
    else:
        form = ClienteForm()
    return render(request, 'registrar_cliente.html', {'form': form})
