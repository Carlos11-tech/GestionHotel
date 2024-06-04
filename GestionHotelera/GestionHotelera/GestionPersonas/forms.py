from django import forms

class ReservationForm(forms.Form):
    name = forms.CharField(label='Nombre')
    email = forms.EmailField(label='Correo electrónico')
    room_type = forms.ChoiceField(label='Tipo de habitación', choices=[('standard', 'Estándar'), ('deluxe', 'Deluxe'), ('suite', 'Suite')])
    services = forms.MultipleChoiceField(label='Servicios adicionales', widget=forms.CheckboxSelectMultiple, choices=[('cleaning', 'Limpieza'), ('bar', 'Bar')])

    # Puedes agregar más campos según sea necesario
