from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ...models import Fund


class ActiveFundListTestCase(TestCase):
    """Test the /api/funds/ endpoint."""

    def setUp(self):
        Fund.objects.create(name="Fund A", strategy="Arbitrage", active=True)
        Fund.objects.create(name="Fund B", strategy="Global Macro", active=True)
        Fund.objects.create(name="Fund C", strategy="Long/Short Equity", active=False)

    def test_list_active_funds(self):
        """Only the active funds are returned."""
        client = APIClient()
        response = client.get("/api/funds/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_funds_by_strategy(self):
        """Strategy filter reduces the number of funds returned."""
        client = APIClient()
        response = client.get("/api/funds/?strategy=Arbitrage")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["strategy"], "Arbitrage")
