from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case
from django.db.models.fields import FloatField
from django.shortcuts import reverse
from pymysql import NULL
from Core.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save


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
    nombre = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    image = models.ImageField(upload_to='producto_images')
    stock = models.IntegerField()
    precio = models.FloatField()
    marca = models.CharField(max_length=150)
    modelo = models.CharField(max_length=150)
    peso_neto = models.CharField(max_length=150)
    unidad_venta = models.CharField(max_length=150)
    oferta = models.IntegerField(default=None)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre) # set the slug explicitly
        super(Producto, self).save(*args, **kwargs) # call Django's save()

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("cart:producto", kwargs={'slug': self.slug})

    

class OrderItem(models.Model):
    orden = models.ForeignKey("Orden", related_name='items', on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"


class Orden(models.Model):
    user = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_orden = models.DateTimeField(blank=True, null=True)
    ordenado = models.BooleanField(default=False)

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

def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.nombre)

pre_save.connect(pre_save_product_receiver, sender = Producto)
