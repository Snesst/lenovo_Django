from django.contrib import admin

# Register your models here. The "Listing" is the same as the class Listing from models.py
from .models import Listing

admin.site.register(Listing)

