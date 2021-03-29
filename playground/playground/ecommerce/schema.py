import graphene
from graphene_django import DjangoObjectType
from ecommerce.models import orders, products

class OrderType(DjangoObjectType):
    class Meta:
        model = orders.Order
        fields = ("id", "user_id", "created_at")

class ProductType(DjangoObjectType):
    class Meta:
        model = products.Product
        fields = ("id", "name", "description", "availability", "image_path")

class Query(graphene.ObjectType):
    all_products = graphene.List(OrderType)

    def resolve_all_products(root, info):
        return orders.Order.objects.all()

schema = graphene.Schema(query=Query)