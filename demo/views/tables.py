import logging
import django_tables2 as tables
from django.utils.html import format_html
from ..models import Fund


logger = logging.getLogger(__name__)


class CurrencyColumn(tables.Column):
    """Formats the Currency as $2.3M."""

    def render(self, value):
        try:
            value_in_millions = f"${value / 1_000_000:.1f}M"
            return format_html(value_in_millions)
        except (ValueError, TypeError) as e:
            logger.error(f"AUM format in db invalid, {e}")
            return "Err"


class FundsTable(tables.Table):
    """Used to display the funds, with pagination."""

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
