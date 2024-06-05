from django.shortcuts import render
from flask import redirect

from Facturacion.models import  Habitacion
from .models import Reserva, CheckIn, CheckOut, Cliente
from django import forms


class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = ['fecha_ingreso', 'hora_ingreso']

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = CheckOut
        fields = ['fecha_salida', 'hora_salida']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'tipo_habitacion', 'tiempo_hospedaje']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_habitacion'].queryset = Habitacion.objects.all()

# Luego en tu vista podrías usar los formularios así:

def crear_reserva(request):
    if request.method == 'POST':
        reserva_form = ReservaForm(request.POST)
        checkin_form = CheckInForm(request.POST)
        checkout_form = CheckOutForm(request.POST)
        if reserva_form.is_valid() and checkin_form.is_valid() and checkout_form.is_valid():
            reserva = reserva_form.save()
            checkin = checkin_form.save(commit=False)
            checkin.reserva = reserva
            checkin.save()
            checkout = checkout_form.save(commit=False)
            checkout.reserva = reserva
            checkout.save()
            return redirect('reserva_exitosa')
    else:
        reserva_form = ReservaForm()
        checkin_form = CheckInForm()
        checkout_form = CheckOutForm()
    return render(request, 'crear_reserva.html', {'reserva_form': reserva_form, 'checkin_form': checkin_form, 'checkout_form': checkout_form})

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'identificacion', 'telefono', 'correo_electronico', 'edad']