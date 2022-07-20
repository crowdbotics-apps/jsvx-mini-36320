from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Firm_companiesViewSet

router = DefaultRouter()
router.register("firm_companies", Firm_companiesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
