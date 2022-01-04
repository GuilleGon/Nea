from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.db.models.expressions import Case
from django.db.models.fields import FloatField

from Core.models import User


class Direccion(models.Model):
    ADDRESS_CHOISES = (
        ('B', 'Billing'),
        ('S', 'Shipping')
    )
    user = models.ForeignKey(User, on_delete=CASCADE)
    dir1 = models.CharField(max_length=100)
    dir2 = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOISES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.dir1}, {self.dir2}, {self.user.codigoPostal}"

    class Meta:
        verbose_name_plural = 'Direcciones'


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    image = models.ImageField(upload_to='producto_images')
    stock = models.IntegerField()
    precio = models.FloatField()
    especificacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class OrderItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"


class Orden(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_orden = models.DateTimeField(blank=True, null=True)
    orden = models.BooleanField(default=False)

    billing = models.ForeignKey(Direccion, related_name='billing_address', blank=True, null=True, on_delete=models.SET_NULL)
    shipping = models.ForeignKey(Direccion, related_name='shipping_address', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"ORDEN-{self.pk}"

class Pago(models.Model):
    order = models.ForeignKey(Orden, on_delete=CASCADE, related_name="pagos")
    metodo = models.CharField(max_length=20, choices=(
        ('Paypal', 'Paypal'),

    ))
    timestamp = models.DateTimeField(auto_now_add=True)
    exitoso = models.BooleanField(default=False)
    monto = FloatField()
    raw_response = models.TextField()
     
    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"PAGO-{self.order}-{self.pk}"