from django.urls import path
from .views import PropertyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'properties', PropertyViewSet, basename='property')

urlpatterns = router.urls