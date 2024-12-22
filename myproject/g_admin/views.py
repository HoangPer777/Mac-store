from django.shortcuts import render

from category.models import Category
from g_admin import templates
from product.models import Product
from coupon.models import Coupon

# Create your views here.
app_name = 'g_admin'


def get_admin(request):
    return render(request, 'g_admin/g_admin.html')


def get_dashboard(request):
    return render(request, 'g_admin/dashboard.html')


def admin_get_product(request):
    products = Product.objects.all().filter(available=True).order_by('-noOfSolds', '-noOfViews')
    total_products = products.count()
    # Tính tổng sản phẩm
    total_products = products.count()
    # Số sản phẩm còn hàng
    in_stock = products.filter(stock_quantity__gt=0).count()
    # Số sản phẩm hết hàng
    out_of_stock = products.filter(stock_quantity=0).count()
    context = {
        'products': products,
        'total_products': total_products,
        'in_stock': in_stock,
        'out_of_stock': out_of_stock,
    }
    return render(request, 'g_admin/ViewCategory.html', context)


def creatProduct(request):
    category = Category.objects.all()
    return render(request, 'product/AddProduct.html', {"category": category})


def get_coupon_list(request):
    coupons = Coupon.objects.all().order_by('-to_date')
    context = {
        'coupons': coupons,
    }
    return render(request, 'g_admin/CouponList.html', context)
