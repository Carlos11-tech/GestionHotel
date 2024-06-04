from django import forms
from .models import Persona, Cliente, Personal, Reserva, CheckOut

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'ID', 'telefono']

class ClienteForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Cliente
        fields = PersonaForm.Meta.fields + ['correoElectronico', 'edad']

class PersonalForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Personal
        fields = PersonaForm.Meta.fields + ['numeroIdentificacion', 'puesto', 'turno']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['tipoHabitacion', 'tiempoHospedaje', 'cliente', 'habitacion']

class CheckOutForm(ReservaForm):
    class Meta(ReservaForm.Meta):
        model = CheckOut
        fields = ReservaForm.Meta.fields + ['fechaSalida', 'horaSalida']
