from django.db import models

class Persona(models.Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=10)

    class Meta:
        abstract = True

class Cliente(Persona):
    # Atributos adicionales
    correo_electronico = models.EmailField(max_length=100)
    edad = models.IntegerField()

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

class CheckIn(models.Model):
    # Atributos
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    hora_ingreso = models.TimeField()

    # Métodos
    def registrar_check_in(self, reserva, fecha_ingreso, hora_ingreso):
        self.reserva = reserva
        self.fecha_ingreso = fecha_ingreso
        self.hora_ingreso = hora_ingreso
        self.save()

class CheckOut(models.Model):
    # Atributos
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()

    # Métodos
    def registrar_check_out(self, reserva, fecha_salida, hora_salida):
        self.reserva = reserva
        self.fecha_salida = fecha_salida
        self.hora_salida = hora_salida
        self.save()

    def actualizar_estado_pago(self):
        pass
