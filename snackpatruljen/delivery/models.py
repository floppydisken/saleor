from saleor.account.models import Address
from saleor.order.models import Order

from django.db import models


class PostalCode(models.Model):
    code = models.TextField("code", blank=False, unique=True, null=False)


class Delivery(models.Model):
    # TODO: Delivery zone should be defined by a google maps zone
    delivery_zones = models.ManyToManyField(PostalCode)
    estimated_time = models.TimeField()
    # TODO:  Default to a warehouse?
    from_address = models.ForeignKey(
        Address, on_delete=models.RESTRICT, related_name="from_address"
    )
    to_address = models.ForeignKey(
        Address, on_delete=models.RESTRICT, related_name="to_address"
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order")
