from django.contrib import messages

from django.core.serializers import json
from django.db.models import Q
from django.utils import timezone

# Create your views here.
from django.shortcuts import render, redirect

from coupon.models import Coupon
from .forms import ProductForm
from .models import Product, ProductImage
from django.http import JsonResponse


def product_list(request, category_id=None):
    coupon = Coupon.objects.filter(type='products', active=True, to_date__gte=timezone.now()).first()

    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()

    context = {
        'products': products,
        'coupon': coupon,
    }
    return render(request, 'product/product_list.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    product.noOfViews += 1
    product.save()
    coupon = Coupon.objects.filter(type='products', active=True, to_date__gte=timezone.now()).first()
    context = {
        'product': product,
        'coupon': coupon,

    }
    return render(request, 'product/productDetail.html', )


# Create
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            product = form.save()
            print(product)
            messages.success(request, "Product created successfully!")
            # return redirect('product_list')
            if 'product_images' in request.FILES:
                for image in request.FILES.getlist('product_images'):
                    ProductImage.objects.create(product=product, image=image)

            return redirect('g_admin:admin_get_product')
        else:
            print(form.errors)
    else:
        return redirect("g_admin:creatProduct")


# Thêm sản phẩm vào giỏ hàng
def cart_add(request, product_id):
    if request.method == 'POST':
        # Lấy giỏ hàng từ session
        cart = request.session.get('cart', {})

        # Thêm sản phẩm vào giỏ hàng
        cart[product_id] = cart.get(product_id, 0) + 1
        request.session['cart'] = cart

        # Tính tổng sản phẩm trong giỏ hàng
        total_items = sum(cart.values())

        # Trả về phản hồi JSON
        return JsonResponse({'success': True, 'total_items': total_items})

    return JsonResponse({'success': False}, status=400)


def total_items_in_cart(request):
    # Lấy giỏ hàng từ session
    cart = request.session.get('cart', {})

    # Tính tổng sản phẩm
    total_items = sum(cart.values())

    # Trả về dữ liệu JSON
    return JsonResponse({'total_items': total_items})


def search(request):
    if request.method == 'GET':
        products = []
        query = request.GET.get('query').strip()

        if query:
            products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

        context = {'query': query, 'products': products}

    return render(request, 'product/searchProduct.html', context=context)
