from django.core.serializers import json
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Product
from django.http import JsonResponse

# Create
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product/AddProduct.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

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
