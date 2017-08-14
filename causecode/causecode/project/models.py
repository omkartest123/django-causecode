from django.db import models

# Create your models here.

class Product(models.Model):
    product_created = models.DateTimeField(auto_now_add = True)
    product_name = models.CharField(max_length = 100, blank = True, default = '')
    product_price = models.IntegerField()
    product_category = models.CharField(max_length = 100, blank = True, default = '')

    class Meta:
        ordering = ('product_created',)