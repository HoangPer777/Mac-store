from django.shortcuts import render

from category.models import Category
from g_admin import templates
from product.models import Product

# Create your views here.
app_name = 'g_admin'
def get_admin(request):

    return render(request, 'g_admin/g_admin.html')

def creatProduct(request):
    category = Category.objects.all()
    return render(request, 'product/AddProduct.html', {"category": category})


def admin_get_product(request):
    products = Product.objects.all().filter(available=True).order_by('-noOfSolds').order_by('-noOfViews')

    context = {'products': products}
    return render(request, 'g_admin/ViewCategory.html', context)




