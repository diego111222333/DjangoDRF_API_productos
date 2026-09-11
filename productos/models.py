# core/models.py
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
    
    def __str__(self):
        return f"{self.nombre} - {self.categoria.nombre}"


class Orden(models.Model):
    ESTADOS = [
        ("enviado", "Enviado"),
        ("entregado", "Entregado"),
        ("rechazado", "Rechazado"),
    ]
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="enviado")
    productos=models.ManyToManyField(Producto, related_name="orden",
    through="DetalleOrden")
    def __str__(self):
        return f"{self.fecha_creacion} - {self.estado}"


class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name="detalles")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,related_name="detalles")
    cantidad = models.PositiveIntegerField(default=1)
    class Meta:
        unique_together = ('producto', 'orden')
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
