from django.contrib.admin import ModelAdmin, site
from .models import Category, Product, ProductAdditions, ProductDeductions


class CategoryAdmin(ModelAdmin):
    list_display = ['title', 'manager']
    list_filter = ['manager']

site.register(Category, CategoryAdmin)


class ProductAdmin(ModelAdmin):
    list_display = ['title', 'stand_category', 'price', 'is_active', 'discount_qty', 'discount_cost']
    list_filter = ['stand_category', 'is_active', 'discount_qty', 'discount_cost']

site.register(Product, ProductAdmin)


class ProductAdditionsAdmin(ModelAdmin):
    list_display = ['product', 'qty', 'cost', 'adder', 'created']
    list_filter = ['product', 'adder', 'created']

site.register(ProductAdditions, ProductAdditionsAdmin)


class ProductDeductionsAdmin(ModelAdmin):
    list_display = ['product', 'qty', 'deductor', 'created']
    list_filter = ['product', 'deductor', 'created']

site.register(ProductDeductions, ProductDeductionsAdmin)
