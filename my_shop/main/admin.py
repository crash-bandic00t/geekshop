from django.contrib import admin
from .models import ProductTypes, Products

# Register your models here.
admin.site.register(ProductTypes)
admin.site.register(Products)