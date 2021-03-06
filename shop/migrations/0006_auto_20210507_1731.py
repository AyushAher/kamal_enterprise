# Generated by Django 3.2.2 on 2021-05-07 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_contact_subj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='dated_created',
            field=models.DateField(default=datetime.datetime(2021, 5, 7, 17, 31, 15, 896730)),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_path',
            field=models.ImageField(upload_to='shop/images/products'),
        ),
    ]
