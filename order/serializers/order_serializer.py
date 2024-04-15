from rest_framework import serializers

from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class OrderSerializer(serializers.ModedlSerializer):
    product = ProductSerializer(required=True, many=True)
    total = serializers.SerializersMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total
    class Meta:
        model = Product
        fields = ['product', 'total']