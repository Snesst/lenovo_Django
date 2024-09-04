from django.contrib import admin

# Register your models here. The "Realtor" is the same as the class Realtor from models.py
from .models import Realtor

admin.site.register(Realtor)

