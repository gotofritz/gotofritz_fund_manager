from django.db import models

STRATEGY_CHOICES = [
    ("Arbitrage", "Arbitrage"),
    ("Global Macro", "Global Macro"),
    ("Long/Short Equity", "Long/Short Equity"),
]


class Fund(models.Model):
    """A single Fund.

    Note that there may be several rows with the same name in the DB,
    but only one would be active. (This is the intention, but due to
    time constraint it is neither validated nor enforced).
    """

    name = models.CharField(max_length=255)
    strategy = models.CharField(max_length=64, choices=STRATEGY_CHOICES, db_index=True)
    aum_usd = models.DecimalField(
        max_digits=16, decimal_places=0, null=True, blank=True
    )
    inception_date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    # allows us to keep a history of past values
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
