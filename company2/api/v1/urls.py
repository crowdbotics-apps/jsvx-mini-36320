from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Company2ViewSet

router = DefaultRouter()
router.register("company2", Company2ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
