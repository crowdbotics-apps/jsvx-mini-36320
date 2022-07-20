from rest_framework import authentication
from company3.models import Company3
from .serializers import Company3Serializer
from rest_framework import viewsets


class Company3ViewSet(viewsets.ModelViewSet):
    serializer_class = Company3Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Company3.objects.all()
