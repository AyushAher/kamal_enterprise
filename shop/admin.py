from django.contrib import admin
from django.utils.translation import ugettext_lazy

# Register your models here.
from . models import *

admin.site.register(Product)
admin.site.register(Order)
# admin.site.register(Stock_inventory)
admin.site.register(Contact)
admin.site.register(OrderUpdate)


admin.site.site_header = "Kamal Enterprises"
admin.site.site_title = "Kamal Enterprises Admin Portal"
admin.site.index_title = "Welcome to Kamal Enterprises Admin Portal"

