# core/urls.py
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProductoViewSet, OrdenViewSet,DetalleOrdenViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'ordenes', OrdenViewSet)
router.register(r'detalles', DetalleOrdenViewSet)

urlpatterns = router.urls
