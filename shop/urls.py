# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   path('privacy/',views.privacy,name='privacy'),
   path('faqs/',views.faqs,name='faqs'),
   path('search/',views.search,name='search'),


   path('tracker/',views.tracker,name='tracker'),
   path('cart/',views.cart,name='cart'),
   path('checkout/',views.checkout,name='checkout'),
   path('productview/<int:id>/',views.productview,name='productview'),
   path('allproduct/',views.products,name='all_product'),
   path('households/',views.households,name='households'),
   path('dry_fruits/',views.dry_fruits,name='dry fruits'),

]