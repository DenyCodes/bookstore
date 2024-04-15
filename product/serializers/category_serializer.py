from rest_framework import serializers

from product.models.product import Product
from product.models.Category import Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'title',
            'description',
            'price',
            'active',
            'category',
        ]