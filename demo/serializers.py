# serializers.py
from rest_framework import serializers
from .models import Fund


class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ["id", "name", "strategy", "aum_usd", "inception_date"]
