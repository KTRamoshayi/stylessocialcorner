# Generated by Django 3.2 on 2021-10-10 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_rename_display_product_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standcategory',
            name='title',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
