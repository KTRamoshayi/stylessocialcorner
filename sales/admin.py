from django.contrib.admin import ModelAdmin, TabularInline, site
from django.db import models
from .models import Sale, SaleItem


class SaleItemInline(TabularInline):
    model = SaleItem
    extra = 5


class SaleAdmin(ModelAdmin):
    list_display = ['id', 'total', 'created']
    list_filter = ['created']
    inlines = [SaleItemInline]

site.register(Sale, SaleAdmin)


# class SaleItemAdmin(ModelAdmin):
#     list_display = ['product', 'sale', 'qty']
#     list_filter = ['sale']
    
# site.register(SaleItem, SaleItemAdmin)
