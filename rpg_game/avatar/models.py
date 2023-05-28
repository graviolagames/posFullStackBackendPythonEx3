from django.db import models


class AvatarClass(models.Model):
    name = models.CharField(max_length=100)
    strength = models.IntegerField()
    ability = models.IntegerField()
    magic = models.IntegerField()
    def __str__(self):
        return self.name
    
class Avatar(models.Model):
    name = models.CharField(max_length=100)
    health = models.IntegerField()
    experience = models.IntegerField()
    reputation = models.IntegerField()
    avatarClass = models.ForeignKey(AvatarClass, on_delete=models.CASCADE)
    Element = models.CharField(max_length=100)
    background = models.TextField()
    def __str__(self):
        return self.name
