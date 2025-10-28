# api/urls.py
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, OrdemProducaoViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')

router.register(r'ordens-producao', OrdemProducaoViewSet, basename='ordemproducao')

urlpatterns = router.urls