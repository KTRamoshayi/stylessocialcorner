# Generated by Django 3.2 on 2021-10-12 05:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='productadditions',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 10, 12, 5, 48, 8, 495170, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productdeductions',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 10, 12, 5, 48, 14, 687794, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
