from django.contrib import admin

from .models.orders import Order
from .models.products import Product

admin.site.register(Order)
admin.site.register(Product)
# Register your models here.
