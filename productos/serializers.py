# core/serializers.py
from rest_framework import serializers
from .models import Categoria, Producto, Orden, DetalleOrden

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id","nombre","descripcion"]
    def validate_nombre(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("El nombre de la categoria no puede contener números.")
        return value

class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    detalle_categoria=CategoriaSerializer(source='categoria', read_only=True)
    class Meta:
        model = Producto
        fields = ["id","nombre","precio","stock","categoria","detalle_categoria"]
    
class DetalleOrdenSerializer(serializers.ModelSerializer):
    producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())
    class Meta:
        model = DetalleOrden
        fields = ["id", "producto","orden","cantidad"]
        read_only_fields = ['orden']
    
class OrdenSerializer(serializers.ModelSerializer):
    detalles = DetalleOrdenSerializer(many=True)
    class Meta:
        model = Orden
        fields = ["id", "fecha_creacion", "estado", "detalles"]
        read_only_fields = ['fecha_creacion']
    #Estas funciones permiten la anidación de objetos 
    def create(self, validated_data):
        detalles_data = validated_data.pop("detalles")
        orden = Orden.objects.create(**validated_data)
        for detalle in detalles_data:
            DetalleOrden.objects.create(orden=orden, **detalle)
        return orden
    def update(self, instance, validated_data):
        detalles_data = validated_data.pop("detalles", None)

        # Actualizo campos simples
        instance.estado = validated_data.get("estado", instance.estado)
        instance.save()

        if detalles_data is not None:
            # Borro los detalles anteriores
            instance.detalles.all().delete()
            # Crea los nuevos
            for detalle in detalles_data:
                DetalleOrden.objects.create(orden=instance, **detalle)

        return instance
