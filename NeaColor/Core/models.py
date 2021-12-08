from django.db import models

class ConsumidorFinal(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cUIT = models.IntegerField()
    domicilio = models.CharField(max_length=100)
    codigoPostal = models.IntegerField()
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    RazonSocial = models.CharField(max_length=100)
    Rubro = models.CharField(max_length=100)
    CUIT = models.IntegerField()
    Domicilio = models.CharField(max_length=100)
    codigoPostal = models.IntegerField()
    Telefono = models.CharField(max_length=20)
    Email = models.CharField(max_length=50)
    def __str__(self):
        return self.RazonSocial