# Generated by Django 3.2 on 2021-10-12 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20211012_0748'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productadditions',
            options={'ordering': ['-pk'], 'verbose_name_plural': 'Product Additions'},
        ),
        migrations.AlterModelOptions(
            name='productdeductions',
            options={'ordering': ['-pk'], 'verbose_name_plural': 'Product Deductions'},
        ),
    ]
