from snackpatruljen.delivery.models import Delivery
import graphene


class DeliveryQuery(graphene.ObjectType):
    delivery = graphene.Field(
        Delivery,
        description="Deliver for order"
    )

    def resolve_delivery(self, info, delivery_id):
        return Delivery.objects.get(pk=delivery_id)
