from rest_framework.routers import DefaultRouter
from .api_views import DeporteViewSet, CanchaViewSet

router = DefaultRouter()
router.register(r"deportes", DeporteViewSet, basename="deporte")
router.register(r"canchas", CanchaViewSet, basename="cancha")

urlpatterns = router.urls
