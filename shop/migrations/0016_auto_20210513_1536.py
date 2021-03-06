# Generated by Django 3.2.2 on 2021-05-13 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20210513_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='dated_created',
            field=models.DateField(default=datetime.datetime(2021, 5, 13, 15, 36, 20, 325451)),
        ),
        migrations.AlterField(
            model_name='orderupdate',
            name='update_desc',
            field=models.CharField(choices=[('Order Placed', 'Order Placed'), ('Order Confirmed & Processing', 'Order Confirmed & Processing'), ('Dispatcted', 'Dispatcted'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], max_length=5000),
        ),
    ]
