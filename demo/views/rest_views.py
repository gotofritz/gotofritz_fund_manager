from demo.models import Fund
from demo.serializers import FundSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveAPIView
from ..models import Fund


class ActiveFundList(ListAPIView):
    """Service endpoint that lists all funds which are active."""

    serializer_class = FundSerializer
    queryset = Fund.objects.filter(active=True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["strategy"]

    def get_queryset(self):
        """
        Restricts the returned funds to a given strategy.

        Example: /api/funds/?strategy=Arbitrage
        """
        queryset = super().get_queryset()
        strategy = self.request.query_params.get("strategy")
        if strategy is not None:
            queryset = queryset.filter(strategy=strategy)
        return queryset


class SingleFund(RetrieveAPIView):
    """Service endpoint that lists a single fund by ID."""

    queryset = Fund.objects.all()
    serializer_class = FundSerializer
