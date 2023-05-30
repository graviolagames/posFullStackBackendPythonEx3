"""
URL configuration for rpg_game project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views import View
from avatar.views import AvatarView
from inventory.views import InventoryView
from inventory.views import InventoryItemView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('avatar/', AvatarView.as_view(), name='avatar'),
    path('inventory/<int:avatar_id>/', InventoryView.as_view(), name='inventory'),
    path('inventory_item/<int:item_id>/', InventoryItemView.as_view(), name='inventoryItem'),
]
