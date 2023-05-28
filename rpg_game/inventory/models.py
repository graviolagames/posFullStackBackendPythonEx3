from django.db import models
from avatar.models import Avatar

# Create your models here.
class InventoryItems(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    carga = models.IntegerField()
    damage = models.IntegerField()
    cure = models.IntegerField()
    def __str__(self):
        return self.name

class Inventory(models.Model):
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE)
    item = models.ForeignKey(InventoryItems, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.avatar.name} - {self.item.name}"