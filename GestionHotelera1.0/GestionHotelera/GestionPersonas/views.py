from django.shortcuts import render, get_object_or_404, redirect
from .forms import PersonaForm, ClienteForm, PersonalForm, ReservaForm, CheckOutForm
from .models import Persona, Cliente, Personal, Reserva, CheckOut


def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'hotel/cliente_form.html', {'form': form})


def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('detalle_cliente', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'hotel/cliente_form.html', {'form': form})

