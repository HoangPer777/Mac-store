from django.shortcuts import render
from django.http import HttpResponse #test
from django.template import loader

from product.models import Product


def get_home(request):
    products = Product.objects.all().order_by('-noOfViews', '-noOfSolds')[:4]
    for product in products:
        products.price = int(product.price)
    return render(request ,'userHome.html' , {'products' :products})

