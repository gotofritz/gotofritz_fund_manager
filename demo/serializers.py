# serializers.py
from rest_framework import serializers
from .models import Fund


class FundSerializer(serializers.ModelSerializer):
    """Used by rest_framework to fetch fields from the DB."""

    class Meta:
        model = Fund
        fields = ["id", "name", "strategy", "aum_usd", "inception_date"]
