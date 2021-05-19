from django.shortcuts import render,HttpResponse,HttpResponsePermanentRedirect
import json
from django.core.mail import send_mail
from django.core.paginator import Paginator
from .models import *
# Create your views here.

def home(request):
    prod=Product.objects.filter(category='households').all()
    prod_paginator=Paginator(prod,6)
    page = prod_paginator.get_page(1)
    
    produ=Product.objects.filter(category='dryfruits').all()
    produ_paginator=Paginator(produ,6)
    page1 = produ_paginator.get_page(1)

    product={
        'page':page,
        'product':prod_paginator.count,
        'page1':page1,
        'product0':produ_paginator.count
    }
    return render(request,'shop/index.html',product)
def search (request):
    pass

def about(request):
    return render(request,'shop/about.html')
    
def privacy(request):
    return render(request,'shop/privacy.html')

def faqs(request):
    return render(request,'shop/faqs.html')

def contact(request):
    if request.method=='POST':
        name= request.POST.get('name','')
        email= request.POST.get('email','')
        phone= request.POST.get('phone','')
        sub=request.POST.get('sub','')
        desc= request.POST.get('desc','')

        con=Contact(name=name,email=email,phone=phone,desc=desc,subj=sub)
        con.save()
        send_mail(sub,desc,'forms.developers.ramson@gmail.com',['developers.ramson@gmail.com'],fail_silently=False)
    return render(request,'shop/mail.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.date_updated})
                    response = json.dumps({"status":"success", "updates": updates,"itemsJson": order[0].items_json }, default=str)
                    
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')

def productview(request,id):
    product=Product.objects.filter(id=id)
    # prod=Product.objects.first()
    # prod_paginator=Paginator(prod,6)
    # page = prod_paginator.get_page(1)
    print(product)
    product={
    'product':Product.objects.filter(id=id),
    # 'page':page,
    # 'prod':prod_paginator.count
    }

    return render(request, 'shop/single.html',product)

def products(request):
    products=Product.objects.all()
    prod_paginator=Paginator(products,6)
    page = prod_paginator.get_page(1)
    product={
        'page':page,
        'product':prod_paginator.count,
    }

    return render(request, 'shop/events.html',product)

def households(request):
    prod=Product.objects.all()
    prod_paginator=Paginator(prod,4)
    page = prod_paginator.get_page(1)

    product={
        'page':page,
        'product':prod_paginator.count
    }
    return render(request,'shop/household.html',product)
    
def dry_fruits(request):
    produ=Product.objects.filter(category='dryfruits').all()
    produ_paginator=Paginator(produ,6)
    page1 = produ_paginator.get_page(1)

    return render(request, 'shop/dryfruit.html')

def cart(request):
    return render(request,'shop/cart.html')

def checkout(request):
   if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '0')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc='Order Placed')
        update.save()
        send_mail(f'New Order from {name}',f'The order is Worth of {amount}','forms.developers.ramson@gmail.com',['developers.ramson@gmail.com'],fail_silently=False)

        thank = True
        return HttpResponsePermanentRedirect('/',{'thank':thank})