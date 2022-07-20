from rest_framework import serializers
from firm.models import Firm_companies


class Firm_companiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm_companies
        fields = "__all__"
