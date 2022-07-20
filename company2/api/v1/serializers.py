from rest_framework import serializers
from company2.models import Company2


class Company2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Company2
        fields = "__all__"
