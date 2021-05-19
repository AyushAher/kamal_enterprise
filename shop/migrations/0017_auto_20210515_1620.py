# Generated by Django 3.2.2 on 2021-05-15 16:20

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20210513_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=10000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='dated_created',
            field=models.DateField(default=datetime.datetime(2021, 5, 15, 16, 19, 36, 799767)),
        ),
    ]
