# Generated by Django 3.2 on 2021-05-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subj',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
