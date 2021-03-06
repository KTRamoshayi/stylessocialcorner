# Generated by Django 3.2.7 on 2021-10-07 13:05

from django.db import migrations, models
import django.db.models.deletion
import sales.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0004_product_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
                ('sale', models.ForeignKey(on_delete=sales.models.Sale, to='sales.sale')),
            ],
        ),
    ]
