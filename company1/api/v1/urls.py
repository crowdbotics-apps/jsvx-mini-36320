from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Company1ViewSet

router = DefaultRouter()
router.register("company1", Company1ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
