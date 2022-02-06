from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Basket

# Register your models here.
@admin.register(Basket)
class BasketAdmin(ModelAdmin):
    list_display = ("id", "user", "product")