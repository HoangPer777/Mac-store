from django.shortcuts import render
from django.http import HttpResponse #test
from django.template import loader

from product.models import Product


def get_home(request):
    top4 = Product.objects.all().order_by('-noOfViews', '-noOfSolds')[:4]
    macPro = Product.objects.all().filter(category_id=1).order_by('-noOfViews', '-noOfSolds')[:8]
    macAir = Product.objects.all().filter(category_id=2).order_by('-noOfViews', '-noOfSolds')[:8]

    context ={
        'top4' :top4,
        'macPro' :macPro,
        'macAir' :macAir
    }
    return render(request ,'userHome.html' , context)

