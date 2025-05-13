from django.db import models

# Create your models here.

class Sucursal(models.Model):
    numero = models.IntegerField(unique=True)
    provincia = models.CharField(max_length=30)
    localidad = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)

    def __str__(self):
        return f"Sucursal {self.numero} - {self.localidad}, {self.provincia}"


class Transporte(models.Model):
    numerotransporte = models.IntegerField(unique=True)
    fechahorasalida = models.DateTimeField()
    fechahorallegada = models.DateTimeField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='transportes')

    def __str__(self):
        return f"Transporte {self.numerotransporte}"


class Repartidor(models.Model):
    numero = models.IntegerField(unique=True)
    dni = models.CharField(max_length=8, unique=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='repartidores')

    def __str__(self):
        return f"Repartidor {self.numero} (DNI: {self.dni})"


class Paquete(models.Model):
    numeroenvio = models.IntegerField(unique=True)
    peso = models.IntegerField()
    nomdestinatario = models.CharField(max_length=60)
    dirdestinatario = models.CharField(max_length=100)
    entregado = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)

    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='paquetes')
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE, related_name='paquetes', null=True, blank=True)
    repartidor = models.ForeignKey(Repartidor, on_delete=models.CASCADE, related_name='paquetes', null=True, blank=True)

    def __str__(self):
        return f"Paquete {self.numeroenvio} para {self.nomdestinatario}"

