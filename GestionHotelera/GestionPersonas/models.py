
from django.db import models

class Persona(models.Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=10)

    class Meta:
        abstract = True

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo_electronico = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    # Métodos
    def registrar_usuario(self, nombre, apellido, identificacion, telefono, correo_electronico):
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.save()

    def login(self, correo_electronico, identificacion):
        return self.correo_electronico == correo_electronico and self.identificacion == identificacion

class Personal(Persona):
    # Atributos adicionales
    numero_identificacion = models.CharField(max_length=10)
    puesto = models.CharField(max_length=50)
    turno = models.CharField(max_length=20)

    # Métodos
    def agendar_hospedaje(self, nombre, apellido, identificacion, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion
        self.telefono = telefono
        self.save()

class Reserva(models.Model):
    tipo_habitacion = models.CharField(max_length=20)
    tiempo_hospedaje = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    checkin = models.OneToOneField('CheckIn', on_delete=models.CASCADE, null=True, blank=True)
    checkout = models.OneToOneField('CheckOut', on_delete=models.CASCADE, null=True, blank=True)

class CheckIn(models.Model):
    # Atributos
    fecha_ingreso = models.DateField()
    hora_ingreso = models.TimeField()

    # Métodos
    def registrar_check_in(self, fecha_ingreso, hora_ingreso):
        self.fecha_ingreso = fecha_ingreso
        self.hora_ingreso = hora_ingreso
        self.save()

class CheckOut(models.Model):
    # Atributos
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()

    # Métodos
    def registrar_check_out(self, fecha_salida, hora_salida):
        self.fecha_salida = fecha_salida
        self.hora_salida = hora_salida
        self.save()

    def actualizar_estado_pago(self):
        pass
