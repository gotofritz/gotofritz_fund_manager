# Generated by Django 4.2.10 on 2024-02-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fund",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "strategy",
                    models.CharField(
                        choices=[
                            ("Arbitrage", "Arbitrage"),
                            ("Global Macro", "Global Macro"),
                            ("Long/Short Equity", "Long/Short Equity"),
                        ],
                        db_index=True,
                        max_length=64,
                    ),
                ),
                (
                    "aum_usd",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=16, null=True
                    ),
                ),
                ("inception_date", models.DateField(blank=True, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
    ]
