# Generated by Django 3.2.7 on 2021-10-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_product_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_qty',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
