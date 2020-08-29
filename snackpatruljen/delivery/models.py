from saleor.account.models import Address
from saleor.order.models import Order
# from saleor.product.models import Product
# from saleor.payment.models import Payment
# from saleor import settings

from django.db import models


class PostalCode(models.Model):
    code = models.TextField("code", blank=False, unique=True, null=False)


class Delivery(models.Model):
    # TODO: Delivery zone should be defined by a google maps zone
    delivery_zones = models.ManyToManyField(PostalCode)
    estimated_time = models.TimeField()
    from_address = models.ForeignKey(
        Address, on_delete=models.RESTRICT, related_name="from_address"
    )
    to_address = models.ForeignKey(
        Address, on_delete=models.RESTRICT, related_name="to_address"
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order")


# class Order(models.Model):
#     pass


# class OrderLine(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="lines")
#     product = models.ForeignKey(Product, on_delete=models.RESTRICT)
#     quantity = models.IntegerField(default=1, blank=False)
#     currency = models.CharField(
#         max_length=settings.DEFAULT_CURRENCY_CODE_LENGTH,
#         default=settings.DEFAULT_CURRENCY,
#     )
#     objects = models.Manager()
#     vat_percentage = 0.25

#     def get_total(self):
#         # TODO: Check whether or not "minimal_variant_price is the correct field"
#         return self.amount * self.product.minimal_variant_price

#     def get_vat_amount(self):
#         return self.get_total() * self.vat_percentage

#     def get_total_with_vat(self):
#         return self.get_total() + self.get_vat_amount()


# class Payment(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     payment = models.ForeignKey(Payment, on_delete=models.RESTRICT)
