"""causecode URL Configuration
lets see

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from causecode.project import views

snippet_list = views.ProductViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'price', views.ProductPriceViewSet)
router.register(r'category', views.CategoryViewSet)
# router.register(r'products/price', views.ProductViewSet.get_price())

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url('^price/(?P<price>.+)/$', views.PriceList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
