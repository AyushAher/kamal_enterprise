# Generated by Django 3.2.2 on 2021-05-08 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210507_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='dated_created',
            field=models.DateField(default=datetime.datetime(2021, 5, 8, 7, 8, 17, 172148)),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/shop/images/products'),
        ),
    ]
