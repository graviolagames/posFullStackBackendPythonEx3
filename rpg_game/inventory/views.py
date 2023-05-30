from django.shortcuts import render
from django.views import View
from .models import Inventory
from .models import InventoryItems
# Create your views here.
class InventoryView(View):
    def get(self, request, avatar_id):
        inventory = Inventory.objects.filter(avatar=avatar_id)
        return render(request, 'inventory/avatar_inventory_list.html', {'inventory': inventory})

class InventoryItemView(View):
    def get(self, request, item_id):
        invItem = InventoryItems.objects.get(id=item_id)
        return render(request, 'inventory/inventory_item.html', {'invItem': invItem})
