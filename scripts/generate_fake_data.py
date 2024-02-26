#! /usr/bin/env python
"""Quick script to generate data for testing pagination.

It prints some CSV rows (default: 50) to the CLI.

Usage:

scripts/generate_fake_data.py 3 > scripts/some.csv

"""


import sys
from faker import Faker

fake = Faker()
STRATEGIES = ["Arbitrage", "Global Macro", "Long/Short Equity"]
MIN_AUM = 123
MAX_AUM = 886


def main(so_many: int):
    """Generate a csv file."""
    fund_names = [f'"{fake.unique.company()} Fund"' for _ in range(so_many)]
    strategies = [f'"{fake.random_element(STRATEGIES)}"' for _ in range(so_many)]
    aums = [
        (
            f'"{fake.random_int(min=MIN_AUM, max=MAX_AUM)}000000"'
            if fake.random.random() > 0.3
            else ""
        )
        for _ in range(so_many)
    ]
    inceptions = [
        (f'"{fake.date(pattern="%Y-%m-%d")}"' if fake.random.random() > 0.3 else "")
        for _ in range(so_many)
    ]
    rows = ['"Name","Strategy","AUM (USD)","Inception Date"'] + [
        f"{name},{strategy},{aum},{inception}"
        for name, strategy, aum, inception in zip(
            fund_names, strategies, aums, inceptions
        )
    ]

    print("\n".join(rows))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            so_many = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid number.")
            sys.exit(1)
    else:
        so_many = 50
    main(so_many)
