""" from rest_framework import routers
from .views import ConciertoViewSet


app_name = "api"
router = routers.DefaultRouter()
router.register("conciertos", ConciertoViewSet, "producto_api")

urlpatterns = router.urls
 """