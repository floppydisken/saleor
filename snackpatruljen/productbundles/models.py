from saleor.product.models import Collection
from saleor import settings

from django.db import models
from django_prices.models import MoneyField


class ProductBundle(Collection):
    currency = models.CharField(max_length=3, default="DKK")
    fixed_price_amount = models.DecimalField(
        max_digits=settings.DEFAULT_MAX_DIGITS,
        decimal_places=settings.DEFAULT_DECIMAL_PLACES,
        default=0,
        editable=False
    )
    fixed_price = MoneyField(
        amount_field="fixed_price_amount",
        currency_field="currency",
    )
