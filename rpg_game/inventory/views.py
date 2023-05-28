from django.shortcuts import render
from django.views import View
from .models import Inventory

# Create your views here.
class InventoryView(View):
    def get(self, request, avatar_id):
        print("avatar_id = ", avatar_id,)
        inventory = Inventory.objects.filter(avatar=avatar_id)
        print("inventory = ",inventory)
        return render(request, 'inventory/avatar_inventory_list.html', {'inventory': inventory})

