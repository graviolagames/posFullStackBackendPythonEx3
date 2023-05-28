from django.contrib.admin import site
from django.contrib import admin
from avatar.models import Avatar
from avatar.models import Class


# Register your models here.
site.register(Avatar)
site.register(Class)

