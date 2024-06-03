from django.db import models
class Persona(models.Model):
    #Atributos
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ID = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)

class Cliente(Persona):
    #atributos
    correoElextrSonico = models.EmailField(max_length=100)
    edad = models.IntegerField()
    #metodos
    def registrarUsuario(self, nombre, apellido, ID, telefono, correoElectronico):
        self.nombre = nombre
        self.apellido = apellido
        self.ID = ID
        self.telefono = telefono
        self.correoElectronico = correoElectronico
        self.save()

    def login(self, correoElectronico, ID):
        if self.correoElectronico == correoElectronico and self.ID == ID:
            return True
        else:
            return False

class Personal(Persona):
    #atributos
    numeroIdentificacion = models.CharField(max_length=10)
    puesto = models.CharField(max_length=50)
    turno = models.CharField(max_length=20)
    #metodos
    def agendarHospedaje(self, nombre, apellido, ID, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.ID = ID
        self.telefono = telefono
        self.save()

class Reserva(Cliente, Personal):
    tipoHabitacion = models.CharField(max_length=20)
    tiempoHospedaje = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Personal, on_delete=models.CASCADE)

class ChekIn(Reserva):
    #Atributos
    fechaIngreso = models.DateField()
    horaIngreso = models.TimeField()
    #Metodos
    def registrarCheckIn(self, nombre, apellido, ID, telefono, correoElectronico, tipoHabitacion,
                         tiempoHospedaje):
        self.nombre = nombre
        self.apellido = apellido
        self.ID = ID
        self.telefono = telefono
        self.correoElectronico = correoElectronico
        self.tipoHabitacion = tipoHabitacion
        self.tiempoHospedaje = tiempoHospedaje
        self.save()

class CheckOut(Reserva):
    #Atributos
    fechaSalida = models.DateField()
    horaSalida = models.TimeField()
    #Metodos
    def registrarCheckOut(self, nombre, apellido, ID, telefono, correoElectronico,
                          tipoHabitacion, tiempoHospedaje):
        self.nombre = nombre
        self.apellido = apellido
        self.ID = ID
        self.telefono = telefono
        self.correoElectronico = correoElectronico
        self.tipoHabitacion = tipoHabitacion
        self.tiempoHospedaje = tiempoHospedaje
        self.save()
    def actualizarEstadoPago(self):
        pass


# Create your models here.
