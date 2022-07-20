from rest_framework import authentication
from firm.models import Firm_companies
from .serializers import Firm_companiesSerializer
from rest_framework import viewsets


class Firm_companiesViewSet(viewsets.ModelViewSet):
    serializer_class = Firm_companiesSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Firm_companies.objects.all()
