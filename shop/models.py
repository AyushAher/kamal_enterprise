from django.db import models
from datetime import datetime
# Create your models here.
class Product(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=10000)
    Volume=models.IntegerField()
    category=models.CharField(max_length=10000 , default="")
    image=models.ImageField(upload_to='static/shop/images/products')
    price=models.IntegerField()
    discount=models.IntegerField()
    uses=models.CharField(max_length=10000)
    Use_Instruction=models.CharField(max_length=10000)
    date_updated=models.DateField()
    
    def __str__(self):
        return self.name
    # stock=models.IntegerField()


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=100000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1110)
    address = models.CharField(max_length=100000)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=6)
    phone = models.CharField(max_length=10)

        
# class Stock_inventory(models.Model):
#     id=models.AutoField

#     product_name=models.CharField(max_length=10000)
#     product_id=models.IntegerField()
#     desc=models.CharField(max_length=10000)
#     qty=models.IntegerField()
#     date_updated=models.DateField()

#     def __str__(self):
#         return self.product_name, self.qty



class OrderUpdate(models.Model):
    desc=[
    ('Order Placed', 'Order Placed'),
    ('Order Confirmed & Processing', 'Order Confirmed & Processing'),

    ('Dispatcted', 'Dispatcted'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered')
    	]
    

    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    update_desc = models.CharField(max_length=5000,choices=desc)
    tracking_no = models.CharField(max_length=1000 ,default="",blank=True)
    date_updated = models.DateField(default=datetime.utcnow())

    def __str__(self):
        return  self.update_desc



class Contact (models.Model):
    id=models.AutoField
    name=models.CharField(max_length=1000)
    email=models.CharField(max_length=1000)
    phone=models.IntegerField()
    subj=models.CharField(max_length=100)
    desc=models.CharField(max_length=10000)
    dated_created=models.DateField(default=datetime.utcnow())
    

    def __str__(self):
        return self.email 