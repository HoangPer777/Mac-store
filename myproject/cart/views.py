from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json

from cart.CartAddProductForm import CartAddProductForm
from cart.models import Cart
from coupon.forms import CouponApplyForm
from product.models import Product


def cart_add(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})

    for item in cart:
        print(item['product'].id)
    coupon_apply_form = CouponApplyForm()
    return render(request, 'cart/Cart.html', {'cart': cart})


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')


def update_quantity(request):
    if request.method == 'POST':
        try:
            # Parse JSON từ request
            data = json.loads(request.body)
            product_id = data.get('product_id')
            new_quantity = data.get('quantity')

            if not product_id or not new_quantity or int(new_quantity) <= 0:
                return JsonResponse({
                    "status": "error",
                    "message": "Invalid product ID or quantity"
                }, status=400)

            cart = Cart(request)
            product = Product.objects.get(id=product_id)

            cart.update(product=product, quantity=new_quantity)

            total_price = product.price * int(new_quantity)

            # Trả về response JSON thành công
            return JsonResponse({
                "status": "success",
                "message": "Quantity updated successfully",
                "data": {
                    "product_id": product_id,
                    "new_quantity": new_quantity,
                    "total_price": total_price
                }
            })
        except Product.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": "Product not found"
            }, status=404)
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": f"An error occurred: {str(e)}"
            }, status=500)
    else:
        return JsonResponse({
            "status": "error",
            "message": "Invalid HTTP method"
        }, status=405)
