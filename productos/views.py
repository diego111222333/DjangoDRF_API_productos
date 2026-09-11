# core/views.py
from rest_framework import viewsets,permissions
from .models import Categoria, Producto, Orden, DetalleOrden
from .serializers import CategoriaSerializer, ProductoSerializer, OrdenSerializer, DetalleOrdenSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    filterset_fields = ['nombre', 'descripcion'] # filtro exacto (M2M funciona igual)
    search_fields = ['nombre'] # búsqueda parcial
    ordering_fields = ['nombre'] # orden
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated] #si se desea proteger una vista especifica, con autenticacion 
    filterset_fields = ['nombre', 'precio'] # filtro exacto (M2M funciona igual)
    search_fields = ['nombre','categoria'] # búsqueda parcial
    ordering_fields = ['nombre'] # orden

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    
    ordering_fields = ['fecha_creacion'] # orden

class DetalleOrdenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DetalleOrden.objects.all()
    serializer_class = DetalleOrdenSerializer
