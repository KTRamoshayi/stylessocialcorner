# Generated by Django 3.2 on 2021-10-07 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20211007_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='available',
            new_name='display',
        ),
    ]