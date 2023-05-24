from django.db import models
# Create your models here.

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_ultima_compra = models.DateField()

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_factura = models.DateField()
    cantidad = models.IntegerField()
    total_factura = models.DecimalField(max_digits=10, decimal_places=2)
