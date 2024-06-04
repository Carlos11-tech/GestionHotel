from django.db import models

class Cargo(models.TextChoices):
    SUPERVISOR = 'SUPERVISOR'
    LIMPIEZA = 'LIMPIEZA'
    COCINA = 'COCINA'
    LAVANDERIA = 'LAVANDERIA'
    CONDUCTOR = 'CONDUCTOR'
    SEGURIDAD = 'SEGURIDAD'
    MASAJISTA = 'MASAJISTA'
    ENCARGADOPISCINA = 'ENCARGADOPISCINA'
    RECEPCIONISTA = 'RECEPCIONISTA'

class Empleado(models.Model):
    cargo = models.CharField(max_length=20, choices=Cargo.choices)
    turno = models.CharField(max_length=50)

class Contratar(models.Model):
    hojaVida = models.TextField()
    terminosCondiciones = models.TextField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

class Administrador(models.Model):
    empleados = models.ManyToManyField(Empleado, through='GestionarEmpleado')

class GestionarEmpleado(models.Model):
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def asignar_sector(self):
        # logic for assigning sector
        pass

    def pagar_sueldo(self):
        # logic for paying salary
        return 0.0