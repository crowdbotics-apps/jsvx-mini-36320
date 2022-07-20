from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Company3ViewSet

router = DefaultRouter()
router.register("company3", Company3ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
