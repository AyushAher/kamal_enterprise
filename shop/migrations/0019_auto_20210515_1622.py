# Generated by Django 3.2.2 on 2021-05-15 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_alter_contact_dated_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='contact',
            name='dated_created',
            field=models.DateField(default=datetime.datetime(2021, 5, 15, 16, 22, 45, 420258)),
        ),
    ]
