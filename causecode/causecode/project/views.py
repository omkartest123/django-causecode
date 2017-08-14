from django.shortcuts import render

# Create your views here.

from causecode.project.models import Product
from rest_framework import viewsets
from causecode.project.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('product_created')
    serializer_class = ProductSerializer