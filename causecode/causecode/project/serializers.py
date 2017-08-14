from causecode.project.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name', 'product_price', 'product_category')

class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name', 'product_price', 'product_category')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name', 'product_price', 'product_category')