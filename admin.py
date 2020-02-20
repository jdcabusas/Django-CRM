from django.contrib import admin

# Register your models here.

from .models import Customer
from .models import Product
from .models import Order

admin.site.register(customer)
admin.site.register(product)
admin.site.register(order)