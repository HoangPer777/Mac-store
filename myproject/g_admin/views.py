from django.shortcuts import render
from g_admin import templates
# Create your views here.
app_name = 'g_admin'
def get_admin(request):

    return render(request, 'g_admin/g_admin.html')

def creatProduct(request):

    return render(request, 'product/AddProduct.html')
