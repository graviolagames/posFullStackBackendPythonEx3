from django.contrib.admin import site
from django.contrib import admin
from inventory.models import Inventory
from inventory.models import InventoryItems

# Register your models here.
site.register(Inventory)
site.register(InventoryItems)

