from django.contrib import admin

from .models import Inventory, PreparationInventory, Product

# Register your models here.

admin.site.register(Inventory)
admin.site.register(PreparationInventory)
admin.site.register(Product)
