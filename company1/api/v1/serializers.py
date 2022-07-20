from rest_framework import serializers
from company1.models import Company1


class Company1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Company1
        fields = "__all__"
