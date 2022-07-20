from rest_framework import serializers
from company3.models import Company3


class Company3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Company3
        fields = "__all__"
