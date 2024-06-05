from django.db import models

class TipoHabitacion(models.TextChoices):
    SUITE = 'SUITE', 'Suite'
    DOBLE = 'DOBLE', 'Doble'
    SENCIL = 'SENCILLA', 'Sencilla'

class TipoPago(models.TextChoices):
    EFECTIVO = 'EFECTIVO', 'Efectivo'
    TRANSFERENCIA = 'TRANSFERENCIA', 'Transferencia'
    TARJETA_CREDITO = 'TARJETA_CREDITO', 'Tarjeta de crédito'
    TARJETA_DEBITO = 'TARJETA_DEBITO', 'Tarjeta de débito'

class Servicios(models.TextChoices):
    SERVICIO_LIMPIEZA = 'SERVICIO_LIMPIEZA', 'Servicio de limpieza'
    SERVICIO_HABITACION = 'SERVICIO_HABITACION', 'Servicio de habitación'
    SERVICIO_GIMNASIO = 'SERVICIO_GIMNASIO', 'Servicio de gimnasio'
    SERVICIO_TV = 'SERVICIO_TV', 'Servicio de TV'
    SERVICIO_WIFI = 'SERVICIO_WIFI', 'Servicio de Wifi'

class Habitacion(models.Model):
    numero = models.IntegerField(unique=True)
    tipo_habitacion = models.CharField(max_length=10, choices=TipoHabitacion.choices)
    estado = models.BooleanField(default=False)  # Por defecto, habitación disponible
    precio = models.FloatField()

    def ocupar(self):
        self.estado = True
        self.save()

    def __str__(self):
        return f"Habitación {self.numero} - {self.tipo_habitacion}"

class Factura(models.Model):
    precio_final = models.FloatField()
    detalles = models.TextField()
    tipo_pago = models.CharField(max_length=15, choices=TipoPago.choices)
    fecha = models.DateTimeField(auto_now_add=True)

    def generar_factura(self, habitacion, numero_huespedes, servicios, precio_final):
        self.habitacion = habitacion
        self.numero_huespedes = numero_huespedes
        self.servicios = servicios
        self.precio_final = precio_final
        self.save()
        return self

    def str(self):
        return f"Factura #{self.id} - Total: {self.precio_final}"