from django.contrib.admin import site
from django.contrib import admin
from avatar.models import Avatar
from avatar.models import Class
from avatar.models import Inventory
from avatar.models import InventoryItems


# Register your models here.
site.register(Avatar)
site.register(Class)
site.register(Inventory)
site.register(InventoryItems)

