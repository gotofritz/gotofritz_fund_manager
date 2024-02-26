import django_tables2 as tables
from django.utils.html import format_html
from .models import Fund


class CurrencyColumn(tables.Column):
    def render(self, value):
        try:
            value_in_millions = f"${value / 1_000_000:.1f}M"
            return format_html(value_in_millions)
        except (ValueError, TypeError):
            return "Err"


class FundsTable(tables.Table):
    aum_usd = CurrencyColumn(verbose_name="AUM (USD)")
    inception_date = tables.DateColumn(format="Y-m-d")

    class Meta:
        model = Fund
        template_name = "django_tables2/gotofritz.html"
        fields = (
            "name",
            "strategy",
            "aum_usd",
            "inception_date",
        )
