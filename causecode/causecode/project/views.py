from django.shortcuts import render

# Create your views here.

from causecode.project.models import Product
from rest_framework import viewsets, generics
from causecode.project.serializers import ProductSerializer, PriceSerializer
from rest_framework.decorators import detail_route	

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('product_created')
    serializer_class = ProductSerializer

class ProductPriceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Products to be viewed according to sorted prices
    """
    queryset = Product.objects.all().order_by('product_price')
    serializer_class = PriceSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Products to be viewed according to sorted categories
    """
    queryset = Product.objects.all().order_by('product_category')
    serializer_class = PriceSerializer

class PriceList(generics.ListAPIView):
    serializer_class = PriceSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        # price = self.kwargs['price']
        queryset = Product.objects.all()
        price = self.request.query_params.get('price', None)
        if price is not None:
        	queryset = queryset.filter(product_price=price)
        return queryset