from django.shortcuts import render, get_object_or_404, redirect
from urllib3 import request

from category.models import Category
from g_admin import templates
from product.models import Product
from coupon.models import Coupon
from django.core.paginator import Paginator

# Create your views here.
app_name = 'g_admin'


def get_admin(request):
    return render(request, 'g_admin/g_admin.html')


def get_dashboard(request):
    # Dữ liệu các sản phẩm bán chạy và nhiều lượt xem
    top_sold_products = Product.objects.all().order_by('-noOfSolds')[:10]
    top_viewed_products = Product.objects.all().order_by('-noOfViews')[:10]

    context = {
        'top_sold_products': top_sold_products,
        'top_viewed_products': top_viewed_products,
    }
    return render(request, 'g_admin/Dashboard.html', context)


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


def createCoupon(request):
    return render(request, 'addCoupon.html')


def get_coupon_list(request):
    coupons = Coupon.objects.all().order_by('-to_date')
    context = {
        'coupons': coupons,
    }
    return render(request, 'g_admin/CouponList.html', context)


from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product
from product.forms import ProductForm  # Form để xử lý sản phẩm


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('g_admin:admin_get_product')
        else:
            print(form.errors)  # In lỗi của form ra console
    else:
        form = ProductForm(instance=product)

    return render(request, 'product/EditProduct.html', {'form': form, 'product': product})
