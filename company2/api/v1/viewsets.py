from rest_framework import authentication
from company2.models import Company2
from .serializers import Company2Serializer
from rest_framework import viewsets


class Company2ViewSet(viewsets.ModelViewSet):
    serializer_class = Company2Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Company2.objects.all()
