from django.db.models import *
from django.contrib.auth.models import User
from django.urls import reverse


class Category(Model):
    title = CharField(max_length=120, unique=True)
    description = TextField()
    manager = ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.title
    
    def return_url(self):
        return reverse('inventory:stand-category-detail', kwargs={'pk': self.pk})
    
    def update_url(self):
        return reverse('inventory:stand-category-update', kwargs={'pk': self.pk})
    
    def delete_url(self):
        return reverse('inventory:stand-category-delete', kwargs={'pk': self.pk})

    def details(self):
        return {
            'title': self.title,
            'description': self.description,
            'manager': self.manager
        }.items()

    class Meta:
        verbose_name_plural = 'Categories'


class Product(Model):
    stand_category = ForeignKey(Category, on_delete=CASCADE)
    title = CharField(max_length=120)
    price = DecimalField(max_digits=5, decimal_places=2)
    discount_qty = PositiveIntegerField(blank=True, null=True)
    discount_cost = DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    description = TextField()
    is_active = BooleanField(default=True)

    def qty(self):
        pass

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class ProductAdditions(Model):
    product = ForeignKey(Product, on_delete=CASCADE)
    cost = DecimalField(max_digits=5, decimal_places=2)
    qty = PositiveIntegerField()
    description = TextField()
    adder = ForeignKey(User, on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name_plural = 'Product Additions'
        ordering = ['-pk']


class ProductDeductions(Model):
    product = ForeignKey(Product, on_delete=CASCADE)
    qty = PositiveIntegerField()
    description = TextField()
    deductor = ForeignKey(User, on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name_plural = 'Product Deductions'
        ordering = ['-pk']
