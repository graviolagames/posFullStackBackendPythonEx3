from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=100)
    strength = models.IntegerField()
    ability = models.IntegerField()
    magic = models.IntegerField()


class InventoryItems(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    carga = models.IntegerField()
    damage = models.IntegerField()
    cure = models.IntegerField()


class Avatar(models.Model):
    name = models.CharField(max_length=100)
    health = models.IntegerField()
    experience = models.IntegerField()
    reputation = models.IntegerField()
    idClass = models.ForeignKey(Class, on_delete=models.CASCADE)
    Element = models.CharField(max_length=100)
    background = models.TextField()
    idInventory = models.ForeignKey(InventoryItems, on_delete=models.CASCADE)
