import logging
from .models import Fund
from django.db import DataError, OperationalError, transaction
from django.core.files.uploadedfile import UploadedFile
from io import TextIOWrapper
import csv
from decimal import Decimal
from datetime import datetime

logger = logging.getLogger(__name__)


def process_uploaded_file(f: UploadedFile) -> str | None:
    """Run simple validation on csv and update database.

    Rows are not overwritten, but simply disabled.
    """
    try:
        text_file = TextIOWrapper(f.file, encoding="utf-8-sig")
        reader = csv.DictReader(text_file)
        uploaded_names = set(
            row["Name"].strip() for row in reader if row["Name"].strip()
        )

        if not uploaded_names:
            logger.error(f"Empty CSV file uploaded")
            return "CSV file is empty"

        text_file.seek(0)
        next(reader)

        with transaction.atomic():
            if uploaded_names:
                Fund.objects.filter(name__in=uploaded_names).update(active=False)

            for row in reader:
                if not row["Name"].strip() or not row["Strategy"].strip():
                    continue

                # Convert 'aum_usd' to Decimal, if present and valid
                aum_usd = None
                if row.get("AUM (USD)"):
                    try:
                        aum_usd = Decimal(row["AUM (USD)"])
                    except ValueError:
                        pass

                inception_date = None
                if row.get("Inception Date"):
                    try:
                        inception_date = datetime.strptime(
                            row["Inception Date"], "%Y-%m-%d"
                        ).date()
                    except ValueError:
                        pass

                Fund.objects.create(
                    name=row["Name"],
                    strategy=row["Strategy"],
                    aum_usd=aum_usd,
                    inception_date=inception_date,
                )
            logger.info(f"Updated {len(uploaded_names) } rows")

    except OperationalError as e:
        msg = f"Couldn't access the database or table: {e}"
        logger.error(msg)
        return msg
    except DataError as e:
        return f"CSV data was decoded, but it is not compatible with DB: {e}"
        logger.error(msg)
        return msg
    except csv.Error as e:
        msg = f"Error processing CSV file: {e}"
        logger.error(msg)
        return msg
    except Exception as e:
        msg = f"There was an error: {str(e)}"
        logger.error(msg)
        return msg
    return None
