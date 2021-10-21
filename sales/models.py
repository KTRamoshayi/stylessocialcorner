from django.db.models import *
from inventory.models import Product
from django.contrib.auth.models import User


class Sale(Model):
    discription = TextField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-pk']
        
    def __str__(self):
        return 'Sale No: ' + str(self.id)

    def total(self):
        total = 0
        for item in self.saleitem_set.all():
            total += item.product.price
        return total
    

class SaleItem(Model):
    sale = ForeignKey(Sale, on_delete=Sale)
    product = ForeignKey(Product, on_delete=CASCADE)
    qty = PositiveIntegerField()

    def __str__(self):
        return self.product.title
