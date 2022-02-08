# Generated by Django 3.2.9 on 2022-02-07 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir1', models.CharField(max_length=100)),
                ('dir2', models.CharField(max_length=100)),
                ('address_type', models.CharField(choices=[('B', 'Billing'), ('S', 'Shipping')], max_length=1)),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Direcciones',
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('fecha_orden', models.DateTimeField(blank=True, null=True)),
                ('ordenado', models.BooleanField(default=False)),
                ('billing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='cart.direccion')),
                ('shipping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='cart.direccion')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('descripcion', models.TextField()),
                ('image', models.ImageField(upload_to='producto_images')),
                ('stock', models.IntegerField()),
                ('precio', models.FloatField()),
                ('marca', models.CharField(max_length=150)),
                ('modelo', models.CharField(max_length=150)),
                ('peso_neto', models.CharField(max_length=150)),
                ('unidad_venta', models.CharField(max_length=150)),
                ('oferta', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo', models.CharField(choices=[('Paypal', 'Paypal')], max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('exitoso', models.BooleanField(default=False)),
                ('monto', models.FloatField()),
                ('raw_response', models.TextField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='cart.orden')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('orden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.producto')),
            ],
        ),
    ]
