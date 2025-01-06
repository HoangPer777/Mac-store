from django.shortcuts import render, get_object_or_404, redirect
from urllib3 import request

from category.models import Category
from coupon.forms import CouponForm
from g_admin import templates
from product.forms import ProductForm
from product.models import Product
from coupon.models import Coupon
from django.core.paginator import Paginator
from django.core.files import File
import requests
from io import BytesIO
from datetime import datetime
from feed_back.models import Feedback
from django.db.models import Q
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


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('g_admin:admin_get_product')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product/EditProduct.html', {
        'form': form,
        'product': product,
        'categories': categories,
    })
    # return render(request, 'product/EditProduct.html', {'form': form, 'product': product})


def remove_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('g_admin:admin_get_product')


def remove_coupon(request, coupon_id):
    coupon = get_object_or_404(Coupon, id=coupon_id)
    coupon.delete()
    return redirect('g_admin:coupon_list')


def get_reviews(request):
    return render(request, 'g_admin/AdminReviews.html')


def admin_feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'g_admin/admin_feedback_list.html', {'feedbacks': feedbacks})


def edit_coupon(request, coupon_id):
    coupon = get_object_or_404(Coupon, id=coupon_id)

    if request.method == "POST":
        form = CouponForm(request.POST, instance=coupon)
        if form.is_valid():
            form.save()
            return redirect('g_admin:coupon_list')  # Redirect về danh sách coupon
    else:
        form = CouponForm(instance=coupon)

    return render(request, 'editCoupon.html', {
        'form': form,
        'coupon': coupon,
    })
def view_category(request):
    search_query = request.GET.get('search', '')
    # Nếu có search_query, lọc sản phẩm
    if search_query:
        products = Product.objects.filter(
            Q(id__icontains=search_query) |  # Tìm theo Product ID
            Q(name__icontains=search_query)  # Tìm theo tên sản phẩm
        )
    else:
        products = Product.objects.all()  # Hiển thị tất cả sản phẩm nếu không tìm kiếm
    total_products = products.count()
    in_stock = products.filter(stock_quantity__gt=0).count()
    out_of_stock = products.filter(stock_quantity__lte=0).count()

    context = {
        'products': products,
        'total_products': total_products,
        'in_stock': in_stock,
        'out_of_stock': out_of_stock,
    }

    return render(request, 'g_admin/ViewCategory.html', context)