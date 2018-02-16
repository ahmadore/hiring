from .models import *
from rest_framework import serializers


class RiskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = ('id', 'title')


class RiskSerializer(serializers.ModelSerializer):
    fields = serializers.JSONField()
    class Meta:
        model = Risk
        fields = "__all__"


class DataStoreSerializer(serializers.ModelSerializer):
    risk = RiskSerializer()
    data_dump = serializers.JSONField()
    
    class Meta:
        model = DataStore
        fields = "__all__"