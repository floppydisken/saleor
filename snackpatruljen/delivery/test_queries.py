import graphene

from graphene import Schema
from graphene.test import Client
from snackpatruljen.delivery.graphql.queries import DeliveryQuery


class Query(graphene.ObjectType):
    greeting = graphene.String(args={"name": graphene.String()})

    def resolve_greeting(self, info, name="you"):
        return f"Hello, {name}"


def test_query():
    client = Schema(Query)
    result = client.execute(
        """
        query DeliveryTest($name: String) {
            greeting(name: $name)
        }
        """,
        variables={"name": "Bob"},
    )
    assert result.data["greeting"] == "Hello, Bob"


def test_get_by_delivery_id():
    client = Schema(DeliveryQuery)
    result = client.execute("""
    query DeliveryQuery(delivery_id: $delivery_id) {
        delivery(delivery_id: $delivery_id)
    }
    """)
    print(result.data["delivery"])
