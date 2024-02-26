from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ...models import Fund


class SingleFundTestCase(TestCase):
    """Test the /api/fund/ endpoint."""

    def setUp(self):
        self.fund = Fund.objects.create(
            name="Fund A", strategy="Arbitrage", active=True
        )

    def test_retrieve_fund(self):
        """An existing fund can be retrieved by id."""
        client = APIClient()
        response = client.get(f"/api/fund/{self.fund.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Fund A")

    def test_retrieve_nonexistent_fund(self):
        """A non existing fund will return a 404 status code."""
        client = APIClient()
        response = client.get("/api/fund/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
