from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json

from cart.CartAddProductForm import CartAddProductForm
from cart.models import Cart
from coupon.forms import CouponApplyForm
from product.models import Product

from django.utils import timezone
from coupon.models import Coupon
from django.http import JsonResponse

from django.db import transaction
from orders.models import Order
from order_detail.models import OrderDetail
from product.models import ProductImage
from decimal import Decimal, InvalidOperation
from django.utils import timezone


def cart_add(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    coupon = Coupon.objects.filter(type='products', active=True, to_date__gte=timezone.now()).first()
    for item in cart:
        product = item['product']
        if (coupon):
            price = item['price']
            value = coupon.percent
            new_price = price - (price * value /100 )
            item['price'] = new_price

        productImage = product.images.first()
        item['productImage'] = productImage.image.url if productImage else None
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


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    # Return updated cart details in the response
    cart_total_price = cart.get_total_price()  # Get the updated total price

    return JsonResponse({
        "status": "success",
        "message": "Item removed successfully",
        "new_total_price": cart_total_price
    })


def total_items_in_cart(request):
    # Lấy giỏ hàng từ session
    cart = request.session.get('cart', {})

    # Tính tổng số lượng sản phẩm
    total_items = sum(item['quantity'] for item in cart.values())

    # Trả về dữ liệu JSON
    return JsonResponse({'total_items': total_items})

# @login_required
# def checkout(request):
#     cart = Cart(request)
#     total_price = cart.get_total_price()
#     return render(request, 'cart/Checkout.html', {'cart': cart, 'total_price': total_price})



def apply_coupon(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            code = data.get('coupon_code')
            # customer_id = data.get('customer_id')
            # product_ids = data.get('product_ids')

            # Kiểm tra mã giảm giá
            coupon = Coupon.objects.filter(
                code=code,
                active=True,
                to_date__gte=timezone.now()
            ).first()
            if not coupon:
                return JsonResponse({"status": "error", "message": "Mã giảm giá không hợp lệ hoặc đã hết hạn."}, status=400)

            cart = Cart(request)
            cart_total = cart.get_total_price()

            # Tính toán giá giảm
            discount_amount = 0
            if coupon.type == 'customer':
                if coupon.percent:
                    discount_amount = (cart_total * coupon.percent) / 100
                    if discount_amount > coupon.maxValue:
                        discount_amount = coupon.maxValue
                if coupon.amount:
                    discount_amount = coupon.amount
            # else:
            #     return JsonResponse({"status": "error", "message": "Không đúng loại."}, status=400)


            ## Tính toán giá giảm
            # discount_amount = (cart_total * coupon.discount) / 100
            # if discount_amount > coupon.maxValue:
            #     discount_amount = coupon.maxValue
            #
            # new_total = cart_total - discount_amount

            # Giảm số lượng mã còn lại
            if coupon.remaining > 0:
                coupon.remaining -= 1
                coupon.save()
            else:
                return JsonResponse({"status": "error", "message": "Mã giảm giá đã hết lượt sử dụng."}, status=400)

            new_total = cart_total - discount_amount
            # Trả về JSON kết quả mới
            return JsonResponse({
                "status": "success",
                "message": "Mã giảm giá đã được áp dụng.",
                "data": {
                    "discount_amount": discount_amount,
                    "new_total": new_total
                }
            })

        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Đã xảy ra lỗi: {str(e)}"}, status=500)



def safe_decimal(value):
    try:
        # Chuyển đổi giá trị thành Decimal nếu hợp lệ
        return Decimal(value)
    except (InvalidOperation, TypeError, ValueError):
        # Nếu lỗi, in log để kiểm tra và trả về giá trị mặc định
        print(f"Invalid Decimal value: {value}")
        return Decimal('0.00')

@transaction.atomic
def process_payment(request):
    if request.method == "POST":
        try:
            cart = Cart(request)
            user = request.user

            if not user.is_authenticated:
                return JsonResponse({"status": "error", "message": "Bạn cần đăng nhập để thanh toán."}, status=401)

            # Lấy mã giảm giá từ POST
            coupon_code = request.POST.get('voucher', None)
            coupon = None

            if coupon_code:
                try:
                    # Kiểm tra mã giảm giá có tồn tại
                    coupon = Coupon.objects.get(code=coupon_code)
                except Coupon.DoesNotExist:
                    coupon = None

            # Tính tổng giá trị giỏ hàng
            total_price = Decimal('0.00')
            for item in cart:
                product = get_object_or_404(Product, id=item['product'].id)
                product_price = safe_decimal(product.price)  # Xử lý giá an toàn
                quantity = safe_decimal(item['quantity'])  # Xử lý số lượng an toàn
                total_price += product_price * quantity  # Tính toán an toàn

            if coupon:
                discount_amount = (total_price * safe_decimal(coupon.discount)) / 100
                if discount_amount > safe_decimal(coupon.maxValue):
                    discount_amount = safe_decimal(coupon.maxValue)
                total_price -= discount_amount

#             if total_price <= 0:
#                 return JsonResponse({"status": "error", "message": "Tổng giá trị không hợp lệ."}, status=400)

            # Tạo đơn hàng
            order = Order.objects.create(
                paymentStatus="Wait",
                dateOrder=timezone.now(),
                totalPrice=total_price,  # Đã được tính toán an toàn
                couponID=coupon,
                paymentMethod=request.POST.get('payment-method', 'Thanh toán khi nhận hàng'),
                userId=user
            )

            # Xử lý chi tiết đơn hàng
            for item in cart:
                product = get_object_or_404(Product, id=item['product'].id)
                quantity = safe_decimal(item['quantity'])

                if product.stock_quantity < quantity:
                    raise ValueError(f"Sản phẩm {product.name} không đủ số lượng.")

                product.stock_quantity -= quantity
                product.noOfSolds += quantity
                product.save()

                OrderDetail.objects.create(
                    order_id=order,
                    product_id=product,
                    quantity=quantity,
                    total_price=safe_decimal(product.price) * quantity
                )

            # Xóa giỏ hàng sau khi thanh toán
            cart.clear()

            return JsonResponse({"status": "success", "message": "Thanh toán thành công."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Đã xảy ra lỗi: {str(e)}"}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Phương thức không hợp lệ."}, status=405)


def thank_you(request):
    return render(request, 'cart/thank_you.html')

def checkout(request):
    cart = Cart(request)
    total_price = cart.get_total_price()
    product_id = request.GET.get('product_id')
    quantity = request.GET.get('quantity', 1)
    address = None
    if request.user.is_authenticated:
        # Giả sử bạn có model Address để lưu địa chỉ của người dùng
        address = request.user.address_set.first()

    for item in cart:
        product = item['product']
        # productImage = product.images.filter(is_primary=True).first()
        productImage = product.images.first()
        item['productImage'] = productImage.image.url if productImage else None

    return render(request, 'cart/Checkout.html', {
        'cart': cart,
        'total_price': total_price,
        'address': address
    })

def checkout_buy_now(request):
    product_id = request.GET.get('product_id')
    quantity = safe_decimal(request.GET.get('quantity', 1))  # Xử lý số lượng an toàn

    if product_id:
        try:
            product = Product.objects.get(id=product_id)
            product_price = safe_decimal(product.price)  # Xử lý giá an toàn
            total_price = product_price * quantity

            cart = [
                {
                    "product": product,
                    "quantity": quantity,
                    "total_price": total_price
                }
            ]

            return render(request, 'cart/Checkout.html', {
                "cart": cart,
                "source": "buy-now",
                "total_price": total_price,
                "user": request.user,
            })

        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Sản phẩm không tồn tại."}, status=404)

    return JsonResponse({"status": "error", "message": "Không có sản phẩm được chọn."}, status=400)


def checkout_view(request):
    source = request.GET.get('source', 'cart')
    product_id = request.GET.get('product_id')
    quantity = int(request.GET.get('quantity', 1))

    if source == 'buy-now' and product_id:
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return HttpResponse("Không tìm thấy sản phẩm", status=404)

        cart = [
            {
                "product": product,
                "quantity": quantity,
                "total_price": product.price * quantity,
            }
        ]
        total_price = sum(item['total_price'] for item in cart)
    else:
        # Xử lý giỏ hàng thông thường
        cart = request.session.get('cart', [])
        total_price = sum(item['total_price'] for item in cart)

    return render(request, 'cart/Checkout.html', {
        "cart": cart,
        "source": source,
        "total_price": total_price,  # Tính tổng giá trị
        "user": request.user,
    })

