from dataclasses import field
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    fields = ['name']
    list_display = ['name', 'slug']


admin.site.register(Products)
