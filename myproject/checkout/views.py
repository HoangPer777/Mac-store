
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from checkout.forms import CheckoutForm
from user.models import User
from address.models import Address
from cart.models import Cart
from coupon.forms import CouponApplyForm

# @login_required
def checkout(request):
    user = request.user
    form = CheckoutForm()
    cart = Cart(request)
    total_price = cart.get_total_price()

    coupon_apply_form = CouponApplyForm()
    # addresses = Address.objects.filter(user=user)
    context = {
        'form': form,
        # 'addresses': addresses,
        'user': {
            'full_name': user.full_name if user.is_authenticated else "Guest",
            # 'addresses': addresses,
            'phone': user.phone if user.is_authenticated else None,

        },
        'cart': cart,
        'total_price': total_price,
        'coupon_apply_form': coupon_apply_form,
    }

    return render(request, 'Checkout.html', context, {'cart': cart, 'total_price': total_price})

def cart_detail(request):
    cart = Cart(request)
    total_price = cart.get_total_price()
    return render(request, 'cart/cart.html', {'cart': cart, 'total_price': total_price})

