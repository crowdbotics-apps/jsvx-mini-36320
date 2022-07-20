from rest_framework import authentication
from company1.models import Company1
from .serializers import Company1Serializer
from rest_framework import viewsets


class Company1ViewSet(viewsets.ModelViewSet):
    serializer_class = Company1Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Company1.objects.all()
